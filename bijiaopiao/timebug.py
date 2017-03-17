#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from datetime import datetime
import time


timedubugstep = {"ddate": "2017-03-01 09:25:00","adate": "2017-03-01 13:40:00"}
durationTime = datetime.strptime(timedubugstep["adate"], '%Y-%m-%d %H:%M:%S') - datetime.strptime(timedubugstep["ddate"], '%Y-%m-%d %H:%M:%S')
print durationTime
timelists = str(durationTime)[0:-3].split(":")
print timelists[0]+'h'+timelists[1]+'m'

numList = timedubugstep["adate"].split(" ")
print numList[0]
print numList[1]
#time.strftime('%Hh%Mm', durationTime)

'''
class HTTPSConnectionV3(httplib.HTTPSConnection):
    def __init__(self, *args, **kwargs):
        httplib.HTTPSConnection.__init__(self, *args, **kwargs)
         
    def connect(self):
        sock = socket.create_connection((self.host, self.port), self.timeout)
        if self._tunnel_host:
            self.sock = sock
            self._tunnel()
        try:
            self.sock = ssl.wrap_socket(sock, self.key_file, self.cert_file, ssl_version=ssl.PROTOCOL_SSLv3)
        except ssl.SSLError, e:
            print("Trying SSLv3.")
            self.sock = ssl.wrap_socket(sock, self.key_file, self.cert_file, ssl_version=ssl.PROTOCOL_SSLv23)
             
class HTTPSHandlerV3(urllib2.HTTPSHandler):
    def https_open(self, req):
        return self.do_open(HTTPSConnectionV3, req)

'''