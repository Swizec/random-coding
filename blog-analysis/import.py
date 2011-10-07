
from pymongo import Connection
from BeautifulSoup import BeautifulSoup
import feedparser
from datetime import datetime

def cleanup(data):
    def cleaned(entry):
        entry.content[0].value = ''.join(BeautifulSoup(entry.content[0].value).findAll(text=True))
        return entry
    data.entries = map(cleaned, data.entries)
    return data

def store(entry, collection):
#    print entry
    print collection.insert({"content": entry.content[0].value,
                             "time": datetime(*list(entry.date_parsed)[:6]),
                             "author": entry.author})

if __name__ == '__main__':
    connection = Connection()
    db = connection.blog_data

    swizec = db['swizec.com']

    data = feedparser.parse('datas/ageekwithahat.wordpress.2011-10-06.xml')
    map(lambda entry: store(entry, swizec),
        cleanup(data).entries)
