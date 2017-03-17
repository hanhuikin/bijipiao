#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import urllib
import urllib2

creatIDUrladdr = 'http://m.ctrip.com/restapi/soa2/10290/createclientid?systemcode=09&createtype=3&head%5Bcid%5D=&head%5Bctok%5D=&head%5Bcver%5D=1.0&head%5Blang%5D=01&head%5Bsid%5D=8888&head%5Bsyscode%5D=09&head%5Bauth%5D=null&head%5Bextension%5D%5B0%5D%5Bname%5D=protocal&head%5Bextension%5D%5B0%5D%5Bvalue%5D=http&contentType=json'

'''
req = urllib2.Request(creatIDUrladdr)
print req

res_data = urllib2.urlopen(req)
res = res_data.read()
print res
'''


def httpGet(urladdr):

    try:
        req = urllib2.Request(creatIDUrladdr)
        res = urllib2.urlopen(req)
        return res

    except Exception as err:

        print err



print httpGet(creatIDUrladdr).read()
#间隔时间转换
def queryDateProcess(quryDate):
    '''
    datetime 改为Year-Month-Day
    '''
    dateStr = quryDate[0:4] + '-' + quryDate[4:6] + '-' +quryDate[6:8]
    return dateStr

print queryDateProcess('20170312')