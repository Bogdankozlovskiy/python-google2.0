# python-google2.0
> sudo pip3 install virtualenv
> sudo pip3 install supervisor
> virtualenv --python=python3.5 myvenv
> source myvenv/bin/activate
> pip install -r requirements.pip
* near settings.py
> vim gunicorn.conf.py
```
bind = '127.0.0.1:6000'
workers = 3
user = "nobody"
```
* sudo vim /etc/supervisor/conf.d/bestproject.conf
```
[program:bestproject]
command=/path/myenv/bin/gunicorn bestproject.wsgi:application -c /path/bestproject/gunicorn.conf.py
directory=/path/
user=nobody
autorestart=true
redirect_stderr=true
```
> service supervisor restart
