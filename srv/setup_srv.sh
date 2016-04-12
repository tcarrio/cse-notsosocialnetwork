# This script assumes a fresh Ubuntu 14.04 Droplet through Digital Ocean

#!/usr/bin/env bash

local START_DIR="$(pwd)"
local REPO_NAME="cse-notsosocialnetwork"
local SRV_PATH="/opt/$REPO_NAME/routes.py"
local PYTHON="python3"
local PIP="pip3"
local TESTING=1

apt-get update
apt-get install -y mysql-server git nginx python3-pip
service nginx stop

if [ ! -d /opt/$REPO_NAME ]
then
    cd /opt
    git clone https://github.com/tcarrio/$REPO_NAME.git
    if [ ! -f /www ]
    then
        ln -s /opt/$REPO_NAME /www
    fi
fi

cd /opt/$REPO_NAME
#$PIP install virtualenv
#virtualenv --no-site-packages venv
#source venv/bin/activate
$PIP install flask flask-login sqlalchemy

#SETUP DATABASE
/www/srv/setup_db.sh

if [ $TESTING==1 ]
then
    #STARTUP ISOLATED FLASK ENVIRONMENT
    local SRV_PID=$($PYTHON $SRV_PATH &)
else
    #STARTUP NGINX WSGI FLASK SERVER
    # configure nginx
    service start nginx
fi