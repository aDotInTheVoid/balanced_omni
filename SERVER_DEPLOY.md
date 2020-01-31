We assume ubuntu 18.04

```bash
git clone https://github.com/aDotInTheVoid/balanced_omni
sudo apt update  # will take some time
sudo apt upgrade
sudo apt install python3-pip 
pip3 install virtualenv
echo 'export PATH="$PATH:$HOME/.local/bin"' >> ~/.bashrc
cd balanced_omni/
virtualenv -p python3 venv
pip install -r requirements.txt
sudo apt-get install nginx
sudo /etc/init.d/nginx start
```
If you now open the ip of the server, you should see a nginx welcome screen
```
pip install uwsgi
./manage.py migrate
```

Now you need to add the ip to the allowed hosts.

Eg: `ALLOWED_HOSTS = ["40.121.193.142"]` is `backend/settings.py`

```
wget https://raw.githubusercontent.com/nginx/nginx/master/conf/uwsgi_params
```
Create a file `balenced_nginx.conf` in the project root.

```
# the upstream component nginx needs to connect to
upstream django {
    # server unix:///path/to/your/mysite/mysite.sock; # for a file socket
    server 127.0.0.1:8001; # for a web port socket (we'll use this first)
}

# configuration of the server
server {
    # the port your site will be served on
    listen      80;
    # the domain name it will serve for
    server_name 40.121.193.142;#example.com; # substitute your machine's IP address or FQDN
    charset     utf-8;

    # max upload size
    client_max_body_size 1M;   # adjust to taste

    # Django media
    location /media  {
        alias /home/nixon/balanced_omni/media;  # your Django project's media files - amend as required
    }

    location /static {
        alias /home/nixon/balanced_omni/static; # your Django project's static files - amend as required
    }

    # Finally, send all non-media requests to the Django server.
    location / {
        uwsgi_pass  django;
        include     /home/nixon/balanced_omni/wsgi_params; # the uwsgi_params file you installed
    }
}
```
sudo cp balenced_nginx.conf /etc/nginx/sites-enabled/
mv uwsgi_params wsgi_params
```
Then add ```STATIC_ROOT = os.path.join(BASE_DIR, "static/")``` to the python settings.
```
./manage.py collectstatic
```

Then set the `django` option in balenced_nginx.conf to 
```
upstream django {
    server unix:///home/nixon/bal.sock; # for a file socket
    #server 127.0.0.1:8001; # for a web port socket (we'll use this first)
}
```