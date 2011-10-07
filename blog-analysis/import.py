
from pymongo import Connection

if __name__ == '__main__':
    connection = Connection()
    db = connection.blog_data

    swizec = db['swizec.com']


