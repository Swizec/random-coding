#!/bin/bash

~/.bin/isightcapture -t jpg ~/tmpTweetAWakeup.jpg
sleep 10
URL=`python ~/Documents/random-coding/TweetAWakeup/upload.py ~/tmpTweetAWakeup.jpg`
twurl tweet -d "status=${URL} #TweetAWakeup"
