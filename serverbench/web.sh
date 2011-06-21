#! /bin/bash
MYSQL="/opt/local/etc/LaunchDaemons/org.macports.mysql5/mysql5.wrapper"
NGINX="/opt/local/sbin/nginx"
PHPFPM="/opt/local/sbin/php-fpm"
PIDPATH="/opt/local/var/run"
MEMCACHED="/opt/local/bin/memcached -m 24 -P /opt/local/var/run/memcached.pid -u root"
 
if [ $1 = "start" ]; then
    sudo $MYSQL start
    echo "Starting php-fpm ..."
    sudo $PHPFPM
    echo "Starting nginx ..."
    sudo $NGINX
    echo "Done!"
elif [ $1 = "stop" ]; then
    echo "Stopping nginx ..."
    sudo kill `cat $PIDPATH/nginx/nginx.pid`
    echo "Stopping php-fpm ..."
    sudo kill `cat $PIDPATH/php-fpm.pid`
    sudo $MYSQL stop
    echo "Done!"
elif [ $1 = "restart" ]; then
    echo "Stopping nginx ..."
    sudo kill `cat $PIDPATH/nginx/nginx.pid`
    echo "Stopping php-fpm ..."
    sudo kill `cat $PIDPATH/php-fpm.pid`
    sudo $MYSQL stop
    sudo $MYSQL start
    echo "Starting php-fpm ..."
    sudo $PHPFPM
    echo "Starting nginx ..."
    sudo $NGINX
    echo "Done!"
elif [ $1 = "nginx" ]; then
    if [ $2 = "start" ]; then
        echo "Starting nginx ..."
        sudo $NGINX
    elif [ $2 = "stop" ]; then
        echo "Stopping nginx ..."
        sudo kill `cat $PIDPATH/nginx/nginx.pid`
    elif [ $2 = "restart" ]; then
        echo "Stopping nginx ..."
        sudo kill `cat $PIDPATH/nginx/nginx.pid`
        echo "Starting nginx ..."
        sudo $NGINX
    else
        echo "Valid commands for nginx: start | stop | restart"
    fi
elif [ $1 = "php" ] || [ $1 = "php-fpm" ]; then
    if [ $2 = "start" ]; then
        echo "Starting php-fpm ..."
        sudo $PHPFPM
    elif [ $2 = "stop" ]; then
        echo "Stopping php-fpm ..."
        sudo kill `cat $PIDPATH/php-fpm.pid`
    elif [ $2 = "restart" ]; then
        echo "Stopping php-fpm ..."
        sudo kill `cat $PIDPATH/php-fpm.pid`
        echo "Starting php-fpm ..."
        sudo $PHPFPM
    else
        echo "Valid commands for php-fpm: start | stop | restart"
    fi
elif [ $1 = "mysql" ]; then
    if [ $2 = "start" ]; then
        sudo $MYSQL start
    elif [ $2 = "stop" ]; then
        sudo $MYSQL stop
    elif [ $2 = "restart" ]; then
        sudo $MYSQL restart
    else
        echo "Valid commands for mysql: start | stop | restart"
    fi
elif [ $1 = "memcached" ]; then
    if [ $2 = "start" ]; then
        sudo $MEMCACHED -d
    elif [ $2 = "stop" ]; then
        sudo kill `cat $PIDPATH/memcached.pid`
        sudo rm $PIDPATH/memcached.pid
    elif [ $2 = "restart" ]; then
        sudo kill `cat $PIDPATH/memcached.pid`
        sudo rm $PIDPATH/memcached.pid
        sudo $MEMCACHED -d
    elif [ $2 = "debug" ]; then
        if [ -e "$PIDPATH/memcached.pid" ]; then
            sudo kill `cat $PIDPATH/memcached.pid`
            sudo rm $PIDPATH/memcached.pid
        fi
        sudo $MEMCACHED -vvv
    else
        echo "Valid commands for memcached: start | stop | restart | debug"
    fi
else
    echo "Valid commands: "
    echo "start | stop | restart"
    echo "----------------------------------------"
    echo "nginx (start | stop | restart)"
    echo "php | php-fpm (start | stop | restart)"
    echo "mysql (start | stop | restart)"
    echo "memcached (start | stop | restart | debug)"
    echo "    Note: Memcached is not run as part of the web stack, it must be started separately."
fi