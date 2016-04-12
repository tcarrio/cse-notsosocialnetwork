#!/usr/bin/env bash

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
    
echo "Executing database setup script\n"
$MYSQL -u $DBUSER "-p$DBPASS" -e "CREATE DATABASE IF NOT EXISTS $DBNAME"
$MYSQL -u $DBUSER "-p$DBPASS" $DBNAME < $SCRIPT_PATH