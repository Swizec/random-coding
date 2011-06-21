#!/bin/bash

## ABSOLUTE path to the PHP binary
PHPFCGI="/usr/local/bin/php"

## tcp-port to bind on
FCGIPORT="8888"

## IP to bind on
FCGIADDR="127.0.0.1"

## number of PHP children to spawn
PHP_FCGI_CHILDREN=5

## number of request before php-process will be restarted
PHP_FCGI_MAX_REQUESTS=1000

# allowed environment variables sperated by spaces
ALLOWED_ENV="ORACLE_HOME PATH USER"

## if this script is run as root switch to the following user
USERID=www-data

################## no config below this line

if test x$PHP_FCGI_CHILDREN = x; then
  PHP_FCGI_CHILDREN=5
fi

ALLOWED_ENV="$ALLOWED_ENV PHP_FCGI_CHILDREN"
ALLOWED_ENV="$ALLOWED_ENV PHP_FCGI_MAX_REQUESTS"
ALLOWED_ENV="$ALLOWED_ENV FCGI_WEB_SERVER_ADDRS"

if test x$UID = x0; then
  EX="/bin/su -m -c \"$PHPFCGI -q -b $FCGIADDR:$FCGIPORT\" $USERID"
else
  EX="$PHPFCGI -b $FCGIADDR:$FCGIPORT"
fi

echo $EX

# copy the allowed environment variables
E=

for i in $ALLOWED_ENV; do
  E="$E $i=${!i}"
done

# clean environment and set up a new one
nohup env - $E sh -c "$EX" &> /dev/null &