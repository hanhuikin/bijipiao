#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import tornado.ioloop
import tornado.web
import json



class hello(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello,xiaorui.cc')
class add(tornado.web.RequestHandler):
    def post(self):
        res = Add(json.loads(self.request.body))
        self.write(json.dumps(res))

def Add(input):
    sum = input['num1'] + input['num2']
    result = {}
    result['sum'] = sum
    return result
application = tornado.web.Application([
    (r"/", hello),
    (r"/add", add),
])

if __name__ == "__main__":
    application.listen(8883)
    print '[+]Server Start'
    tornado.ioloop.IOLoop.instance().start()
#大家可以写个form测试，也可以用curl -d测试