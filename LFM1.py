#coding = utf-8
import pandas as pd
import numpy as np
import math 
import random
import pickle
import os
import csv


#coding = utf-8
import pandas as pd
import numpy as np
import math 
import random
import pickle
import os
import csv

def ItemUserMatrix(root,result):
    user_dict = dict()              # user_id �������ֵ�
    jd_dict = dict()                #jd_poi �������ֵ�
    jd_users_dict = dict()          #ÿ��jd ��Ӧ�� ȥ���ι����������۹����û���id
    user_jds_dict = dict()          #ÿ��userȥ�������۵�jd��poi
    n = 0                           # user_id �������ֵ��е���������
    m = -1                          #jd_poi �������ֵ��е���������
    mat = np.full((30000,3000),0.65)   #ÿһ�д����û��Լ����������������
    rpath = os.path.join(root, 'new1.csv')
    with open(rpath, 'rb') as cf:                                                                    
        df = pd.DataFrame(pd.read_csv(cf, encoding="unicode_escape", lineterminator= '\n'))
    M = df.as_matrix()      #��Dataframe����ת��Ϊ������ʽ
    for x in range(len(M)):
        jd = str(M[x][2])     #��ÿ�������jd_poi��ȡ������ת�����ַ���       
        if jd not in jd_dict.keys():
            m += 1
            jd_dict[jd] = m
        #����jd_users_dict�ֵ�
        if m not in jd_users_dict.keys():                                                          
            jd_users_dict[m] = set()
                #��ȡuser_id���������ַ�����ͬʱ��jd_users_dict������û�
            I = str(M[x][0])
            if I not in user_jds_dict.keys():
                user_jds_dict[n] = set()
            #user�����ֵ丳ֵ�����Ҷ�mat��ֵ
            if I not in user_dict.keys():                                                           
                user_dict[I] = n
                jd_users_dict[m].add(n)
                user_jds_dict[n].add(m)
                a = 0
                a = M[x][3]
                b = a/5         #�����ֵ��������������
                mat[n][m] = b
                n += 1
                x += 1
            else:
                c = user_dict[I]
                jd_users_dict[m].add(c)
                user_jds_dict[c].add(m)
                a = 0
                a = M[x][3]
                b = a/5         #�����ֵ��������������
                mat[c][m] = b
                x += 1 
        else:
            I = str(M[x][0])
                
            if I not in user_jds_dict.keys():
                user_jds_dict[n] = set()
            #user�����ֵ丳ֵ�����Ҷ�mat��ֵ
            if I not in user_dict.keys():
                user_dict[I] = n
                jd_users_dict[m].add(n)
                user_jds_dict[n].add(m)
                a = 0
                a = M[x][3]
                b = a/5         #�����ֵ��������������
                mat[n][m] = b
                n += 1
                x += 1
            else:
                c = user_dict[I]
                jd_users_dict[m].add(c)
                user_jds_dict[c].add(m)
                a = 0
                a = M[x][3]
                b = a/5         #�����ֵ��������������
                mat[c][m] = b
                x += 1
    #���õ�������д���ļ�
    print(n)
    print(m)
    user_dict_path = os.path.join(result, 'user_dict')
    jd_dict_path = os.path.join(result, 'jd_dict')
    jd_users_dict_path = os.path.join(result, 'jd_users_dict')
    user_jds_dict_path = os.path.join(result, 'user_jds_dict')
    ItemUserMatrix_path = os.path.join(result, 'ItemUserMatrix')
   
    with open(user_dict_path, 'wb') as uf:
        pickle.dump(user_dict, uf)
    with open(jd_dict_path, 'wb') as jf:
        pickle.dump(jd_dict, jf)
    with open(jd_users_dict_path, 'wb') as juf:
        pickle.dump(jd_users_dict, juf)
    with open(user_jds_dict_path, 'wb') as ujf:
        pickle.dump(user_jds_dict, ujf)
    np.save(ItemUserMatrix_path,mat)

def SelectNagativeSample(user, items,ItemUserMatrix): #��ѡ��������
    ret = dict()
    n = 0
    for i in items:
        ret[i] = 1
        n += 1
    I = ItemUserMatrix[user].argsort()
    for j in I:
        if j in items:
            continue
        ret[j] = 0
        n -= 1
        if n == 0:
            break
    return ret

def InitModel(result, F):
    user_factor_matrix_path = os.path.join(result, 'user_factor_matrix.npy')
    jd_factor_matrix_path = os.path.join(result, 'jd_factor_matrix.npy')
    ItemUserMatrix_path = os.path.join(result, 'ItemUserMatrix.npy')
    
    ItemUserMatrix = np.load(ItemUserMatrix_path)
    P = np.random.randn(F,len(ItemUserMatrix))  #* 0.01
    Q = np.random.randn(F,len(ItemUserMatrix[0])) #* 0.01
    
    np.save(user_factor_matrix_path, P)
    np.save(jd_factor_matrix_path, Q)


def predict(user, item, P, Q):
    P = np.transpose(P)
    r = (P[user] * Q[:,item]).sum() * 0.01
    return r

def LantentFactorModel(result, N, alpha, l):
    
    user_jds_dict_path = os.path.join(result, 'user_jds_dict')
    ItemUserMatrix_path = os.path.join(result, 'ItemUserMatrix.npy')
    user_factor_matrix_path = os.path.join(result, 'user_factor_matrix.npy')
    jd_factor_matrix_path = os.path.join(result, 'jd_factor_matrix.npy')
    
    user_items_dict = np.load(user_jds_dict_path)
    ItemUserMatrix = np.load(ItemUserMatrix_path)
    P = np.load(user_factor_matrix_path)
    Q = np.load(jd_factor_matrix_path)
    
    for step in range(0,N):
        for user,items in user_items_dict.items():
            samples = SelectNagativeSample(user, items, ItemUserMatrix)
            for item, rui in samples.items():
                eui = rui - predict(user, item, P, Q)
                for f in range(len(P)):
                    P[f][user] += alpha * (eui * Q[f][item] - (l * P[f][user]))
                    Q[f][item] += alpha * (eui * P[f][user] - (l * Q[f][item]))
        alpha *= 0.9
        print(str(step) + 'Done')
    
    np.save(user_factor_matrix_path, P)
    np.save(jd_factor_matrix_path, Q)


ItemUserMatrix(root,result)
InitModel(result, 100)

LantentFactorModel(result, 10, 0.02, 0.01)