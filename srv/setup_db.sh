#!/usr/bin/env bash
set +e # turn off errexit
setupDB(){
    local DBUSER="root"
    local DBPASS="nssntest"
    local SCRIPT_PATH="/www/srv/setup_db.sql"
    local MYSQL="mysql"
    local DBNAME="nssndb"

    local MYSQL_PATH="$(which $MYSQL)"

    if [ ! -f  "$MYSQL_PATH" ] 
    then
        printf "%s was not found in your PATH variable. Please check your PATH configuration.\n" "$MYSQL"
        exit 1
    else
        local MYSQL="$MYSQL_PATH"
    fi

    echo "Executing database setup script"
    $MYSQL -u $DBUSER "-p$DBPASS" -e "CREATE DATABASE IF NOT EXISTS $DBNAME"
    $MYSQL -u $DBUSER "-p$DBPASS" -e "CREATE USER 'nssnuser'@'%' IDENTIFIED BY 'nssnpass';"
    $MYSQL -u $DBUSER "-p$DBPASS" -e "GRANT ALL PRIVILEGES ON *.* TO 'nssnuser'@'%'"
    $MYSQL -u $DBUSER "-p$DBPASS" $DBNAME < $SCRIPT_PATH
}
setupDB