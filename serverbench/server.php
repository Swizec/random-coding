<?php

$redis = new Redis();

$redis->connect('127.0.0.1', 6379);

echo $HTTP_RAW_POST_DATA;

$redis->close();

?>