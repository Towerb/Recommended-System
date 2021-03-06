<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ page language="java" contentType="text/html; charset=UTF-8"
         pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
    <title>管理员接口 - 旅游推荐系统</title>
    <link href="http://g.alicdn.com/sj/dpl/1.5.1/css/sui.min.css" rel="stylesheet">
    <%--<script type="text/javascript" src="http://g.alicdn.com/sj/dpl/1.5.1/js/sui.min.js"></script>--%>
    <link rel="stylesheet" href="//apps.bdimg.com/libs/jqueryui/1.10.4/css/jquery-ui.min.css">
    <link rel="stylesheet" href="../css/bootstrap.min.css">
    <link rel="stylesheet" href="../css/main.css">
    <script src="../js/jquery-3.3.1.min.js"></script>
    <script src="../js/jquery.cookie.js"></script>
    <script src="../js/searchTicket.js"></script>
    <%--jQuery顺序要在jQuery-ui前面--%>
    <script src="//apps.bdimg.com/libs/jqueryui/1.10.4/jquery-ui.min.js"></script>

    <script>
        $(function () {
            $("#datepicker").datepicker();
        });
    </script>

</head>

<body>
<div class="navbar navbar-default">
    <div class="container">
        <div class="navbar-header">
            <a href="/admin/form-amazeui.jsp" class="navbar-brand"></a>
        </div>
        <ul class="nav navbar-nav">
            <li><a href="/refreshticket" title="刷新车票">管理员临时操作界面</a></li>
        </ul>
    </div>
</div>

<div class="container">
    <div class="form-container">
        <br/>
        <br/>
        <br/>
        <br/>
        <h1 style="text-align: center">管理员操作接口</h1>
        <br/>
        <br/><br/>
        <form method="get" action="/refreshticket">
            <div class="form-group">
                <button id="gen" type="submit" class="btn btn-primary btn-block">点击一键生成预售期车票</button>
            </div>
        </form>
    </div>
</div>

<div class="footer">
    © 2019 基于隐语义模型的旅游推荐系统
</div>
</body>
</html>
