#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import tornado.ioloop
import tornado.web
import json
from sectrip import *
from sequna import *
from quanh5 import *
from Log import *



class cid(tornado.web.RequestHandler):
    def get(self):
        cid = genCid()
        self.write(json.dumps(cid))

class queryFlight(tornado.web.RequestHandler):
    def post(self):
        try:
            res = queryFlightList(json.loads(self.request.body))
            self.write(json.dumps(res))
        except Exception as err:
            print err
            pass

class refundChange(tornado.web.RequestHandler):
    def post(self):
        res = queryRefundChange(json.loads(self.request.body))
        self.write(json.dumps(res))

class queryQunaFlight(tornado.web.RequestHandler):
    def post(self):
        res = queryQunaFlightList(json.loads(self.request.body))
        self.write(json.dumps(res))


class queryQunaRefundChang(tornado.web.RequestHandler):
    def post(self):
        res = queryQunaRefundChangList(json.loads(self.request.body))
        logging.info(res)
        self.write(json.dumps(res))

application = tornado.web.Application([
    (r"/cid", cid),
    (r"/queryFlight", queryFlight),
    (r"/refundChange", refundChange),
    (r"/queryQunaFlight", queryQunaFlight),
    (r"/queryQunaRefundChang", queryQunaRefundChang)
])


if __name__ == "__main__":
    application.listen(8886)
    print '[+]Server Start'
    logfileName = 'Daily.log'
    logFilePath = os.path.join(os.path.dirname(__file__),logfileName)
    CreatFile(logFilePath)
    logBasicSetting(logFilePath)

    tornado.ioloop.IOLoop.instance().start()