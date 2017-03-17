#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import httplib,urllib2
import json
from flightValues import *
from datetime import datetime
import time
import re
# Post 
def httpPost(urlAddr, postContent):

    headers = {'Content-Type':'application/json'}

    try:

        ParamesJson = json.dumps(postContent)
        
        req = urllib2.Request(urlAddr, ParamesJson, headers)

        res = urllib2.urlopen(req)
        
        return res

    except Exception as err:

        print err
        pass



if __name__ == "__main__":

	urllss = 'http://127.0.0.1:8886/queryQunaFlight'

	datess = {"oragin":"北京","dest":"广州", "tripType":"1","fromDate":"20170318"}

	resss = httpPost(urllss, datess)

	print resss.read()
	dix = json.loads(resss.read())

	print dix['fromSegments'][0]['pid']
	print type(dix['fromSegments'][0]['pid'])



