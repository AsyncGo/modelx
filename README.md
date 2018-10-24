# modelx
## 基于falsk框架的python-web项目，实现实时模型计算，离线任务治理等。
### 部署：
    nginx+uwsgi 
### nginx配置（测试）：
    ```
    server {
        listen       8080;
        server_name  localhost;
        #charset koi8-r
        location / {
            include uwsgi_params;
            uwsgi_pass unix:/home/work/nginx/uwsgi/uwsgi.sock;
        }
        #error_page  404              /404.html;
        # redirect server error pages to the static page /50x.html
        #
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }
     }
     ```
### uwsgi配置(测试)：
      ```
      [uwsgi]
      home = /home/work/python3/
      pythonpath = /home/work/flask
      app = manage
      module = %(app)
      callable = app
      master=true
      processes=4
      chmod-socket=666
      logfile-chmod=644
      py-autoreload=1
      #http=0.0.0.0:8081
      vacuum=true
      chdir=/home/work/nginx/uwsgi
      socket=%(chdir)/uwsgi.sock
      stats=%(chdir)/uwsgi.status
      pidfile=%(chdir)/uwsgi.pid
      daemonize=%(chdir)/uwsgi.log
      ```
