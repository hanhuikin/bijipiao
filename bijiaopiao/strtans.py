#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import json

ss ={"arrCity": u"\u4e0a\u6d77","dd":}

print type(ss['arrCity'])
print type(ss['arrCity'].encode("utf-8"))

value = dict()
print value

#rr = {'pid': {'goDate': '2017-03-16', 'depArr': 'ea733a43304e307ca36d4a1b8e8a3e5ca274e5dbf12422f6ea156afc2bc3ee9ae1a1571b26afe2c13fea1c7948d6a950', 'arrCity': '\u4e0a\u6d77', 'depCity': '\u5317\u4eac', 'flightNo': 'CZ6412'}, 'cid': ''}
#ssa  = json.dumps(rr)
#print json.loads(rr)


df = {}

cds = json.dumps(df)

print type(cds)

print json.loads(cds)