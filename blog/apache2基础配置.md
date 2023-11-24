## apache2_base_config
* 服务使用linux的systemctl命令控制，每次修改配置后要重启服务器才能生效
* sudo apt install apache2 安装
* 默认站点发布目录为/var/www
* 配置目录：
```bash
/etc/apache2/   
       |-- apache2.conf  
       |       `--  ports.conf   
       |-- mods-enabled   
       |       |-- *.load   
       |       `-- *.conf   
       |-- conf-enabled   
       |       `-- *.conf   
       `-- sites-enabled   
               `-- *.conf  
```
* mods-enable文件夹中是mods-avalible中的启用模块的软链接，如果想给apache2添加什么功能模块，直接建立一个从avalible中建立一个快捷方式到enabled中就行
* sites-enabled和sites-avablible同理，sites-enabled中的000-default.conf是是avalible文件夹中000-default.conf的软链接，avalible文件夹中还有一个default-ss.conf，是用于设置ssh证书网站的。
* 主文件000-default.conf内容：
```bash 
<VirtualHost *:80>
        # The ServerName directive sets the request scheme, hostname and port that
        # the server uses to identify itself. This is used when creating
        # redirection URLs. In the context of virtual hosts, the ServerName
        # specifies what hostname must appear in the request's Host: header to
        # match this virtual host. For the default virtual host (this file) this
        # value is not decisive as it is used as a last resort host regardless.
        # However, you must set it for any further virtual host explicitly.
        #ServerName www.example.com

        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/html

        # Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
        # error, crit, alert, emerg.
        # It is also possible to configure the loglevel for particular
        # modules, e.g.
        #LogLevel info ssl:warn

        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
        # For most configuration files from conf-available/, which are
        # enabled or disabled at a global level, it is possible to
        # include a line for only one particular virtual host. For example the
        # following line enables the CGI configuration for this host only
        # after it has been globally disabled with "a2disconf".
        #Include conf-available/serve-cgi-bin.conf
</VirtualHost>

# vim: syntax=apache ts=4 sw=4 sts=4 sr noet

```

* ServerAdmin： 设置一个邮件地址，如果服务器有任何问题将发信到这个地址， 这个地址会在服务器产生的某些页面中出现。
* DocumentRoot 是这个站点的根目录,即为80端口的默认访问目录
* 配置站点的入口文件：在/etc/apache2/mods-available/dir.conf文件中。默认显示有：index.html index.cgi index.pl index.php index.xhtml index.htm
