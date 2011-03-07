
import urllib2, base64, urllib, json, sys
from datetime import datetime

if __name__ == '__main__':
    print json.loads(urllib2.urlopen('http://api.imgur.com/2/upload.json',
                                     data=urllib.urlencode({
                                         'key': '927ff7a7e84621a6371c2f0aaf8dc770',
                                         'image': base64.encodestring(
                                             open(sys.argv[1]).read()),
                                         'type': 'base64',
                                         'name': 'TweetAWakeup: '+str(datetime.now()),
                                         'title': 'TweetAWakeup: '+str(datetime.now())
                                         })).read())['upload']['links']['imgur_page']
