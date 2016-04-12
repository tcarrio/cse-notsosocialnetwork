# This script assumes a fresh Ubuntu 14.04 Droplet through Digital Ocean
MYSQL_PWD="nssntest"
export MYSQL_PWD

#!/usr/bin/env bash
main(){
    local START_DIR="$(pwd)"
    local REPO_NAME="cse-notsosocialnetwork"
    local SRV_PATH="/opt/$REPO_NAME/routes.py"
    local PYTHON="python3"
    local PIP="pip3"
    local TESTING=1
    local MY_IP=$(dig +short myip.opendns.com @resolver1.opendns.com)

    apt-get update
    apt-get install -y mysql-server git nginx python3-pip vim
    service nginx stop

    if [ ! -d /opt/$REPO_NAME ]
    then
        cd /opt
        git clone https://github.com/tcarrio/$REPO_NAME.git
        printf '\n    EXT_IP="$MY_IP"' >> $REPO_NAME/config/env_config.py
    fi
    
    if [ ! -f /www ]
    then
        ln -s /opt/$REPO_NAME /www
    fi

    cd /www
    #$PIP install virtualenv
    #virtualenv --no-site-packages venv
    #source venv/bin/activate
    $PIP install flask sqlalchemy pymysql

    #SETUP DATABASE
    chmod +x /www/srv/*
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
}
main
