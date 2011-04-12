import tornado.ioloop
import tornado.web

import json, redis

r = redis.Redis(host='localhost', port=6379, db=0)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

    def post(self):
        data = json.loads(self.request.body)
        value = r.get(data['key'])
        r.set(data['key'], data['value'])
        self.write(value)

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8124)
    tornado.ioloop.IOLoop.instance().start()
