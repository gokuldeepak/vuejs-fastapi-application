1) Create a VM in Virtualbox with ubuntu 20.04 iso image and use  bridged adapter to acces it from local host putty session.

2) Install dependencies:

 Commands to install Docker:

 sudo apt install docker-compose
 sudo usermod -aG docker $USER
 sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
 sudo service docker restart

sudo su
apt install npm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash
source ~/.bashrc
nvm list-remote
nvm install v14.10.0
nvm list
npm install -g @vue/cli@5.0.8
vue -V



Document followed for this test development:
https://testdriven.io/blog/developing-a-single-page-app-with-fastapi-and-vuejs/