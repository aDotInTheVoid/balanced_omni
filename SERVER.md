# Deploying to a server.

Create an azure ubuntu 18.04 vm with a user called `webman` who has root.

SSH into the vm.

```bash
sudo apt update # This may stall, so you might need to ^C it and run again
sudo apt upgrade
sudo apt install nginx python3-pip uwsgi uwsgi-plugin-python3
git config --global credential.helper cache
git config --global credential.helper 'cache --timeout=360000'
git clone https://github.com/aDotInTheVoid/balanced_omni
cd balanced_omni
pip3 install virtualenv
echo 'export PATH="$PATH:$HOME/.local/bin"' >> ~/.bashrc
source ~/.bashrc
virtualenv -p python3 venv
source  venv/bin/activate
pip install -r requirements.txt
./manage.py collectstatic
./manage.py migrate
./manage.py createsuperuser # Fill in details
deactivate
sudo -H ln -s $HOME/balanced_omni/server/site_nginx.conf /etc/nginx/sites-enabled/
sudo /etc/init.d/nginx restart
uwsgi --ini ~/balanced_omni/server/uwsgi.ini # This needs to be backgrounded, and I'm not sure how to yet
```
