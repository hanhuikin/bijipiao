 #!/usr/bin/python

#-*- coding: utf-8 -*-
__author__ = 'stone'
import tornado.ioloop
import pyrestful.rest
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
import logging
from common.Log import LogInit
from common.Cfg import config
from business.Customer import CustomerResource
LogInit("loggingREST.conf")
cfg = config(filename="config4REST.conf")
#a list to route different REST Service.
restservices = []
restservices.append(CustomerResource)
if __name__ == "__main__":
    loggerRoot = logging.getLogger('root')
    loggerRoot.debug("start run REST module.")
    try:
        app = pyrestful.rest.RestService(restservices)
        port = cfg.get('port','port')
        app.listen(port)
        tornado.ioloop.IOLoop.instance().start()
    except Exception,ex:
        pass