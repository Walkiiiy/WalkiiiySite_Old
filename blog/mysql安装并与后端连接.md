## 安装
* sudo apt install mysql-server
* sudo mysql_secure_installation 完成一些安全措施，包括设置root用户的密码、删除匿名用户、禁止root用户远程登录，以及删除测试数据库。
* systemctl status mysql.service 查看状态
* sudo systemctl start mysql 启动服务
* sudo mysql -u root -p 登陆
* sudo apt install mysql-workbench 安装图形管理界面
## 修改密码
* sudo mysqld_safe --skip-grant-tables &   安全模式启动sql
* mysql -u root
* USE mysql;
* UPDATE user SET plugin='mysql_native_password' WHERE User='root'; 更改身份验证方法
* SET GLOBAL validate_password.policy=LOW; 降低密码等级
* FLUSH PRIVILEGES;
ALTER USER 'root'@'localhost' IDENTIFIED BY 'new_password';设置新密码






