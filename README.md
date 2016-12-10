# Flasky



* 基于Python **Flask**框架的博客程序

* 参考*《O'REILLY 系列丛书 Flask Web开发》*--基于Python的Web应用开发实战

* 完成于2016年12月10日

##安装方法

1.  安装虚拟环境，执行```pip install -r requirements.txt```进行环境配置
2.  修改```config.py```中的数据库地址进行连接数据库并修改```FLASKY_ADMIN```选项为管理员的邮箱
3.  执行```python manage.py db init```初始化数据库
4.  执行```python manage.py db migrate```提交数据库版本
5.  执行```python manage.py db upgrade```更新数据库信息
6.  执行```python manage.py shell```打开Shell 并执行```Role.insert_roles()```更新用户角色信息
7.  执行```python manage.py runserver```进行启动服务器
8.  使用```FLASKY_ADMIN```中填写的用户进行注册
