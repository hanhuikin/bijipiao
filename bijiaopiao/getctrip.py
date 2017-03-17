import urllib
import urllib2
import json

requetdata = {"preprdid":"","trptpe":"2","flag":8,"seat":0,"extendinfo":[{"extype":5,"expam":1}],
"searchitem":[{"dccode":"SHA","accode":"SZX","dtime":"2017-03-09"},
{"dccode":"SZX","accode":"SHA","dtime":"2017-03-10"}],
"sflgno":"","head":{"cid":"09031015111440212896","ctok":"",
"cver":"1.0","lang":"01","sid":"8888","syscode":"09","auth":None,"extension":[{"name":"protocal","value":"http"}]},
"contentType":"json"}
urlladdr = 'https://sec-m.ctrip.com/restapi/soa2/11781/Domestic/FlightList/Query?_fxpcqlniredt=09031133310129490276'
headers = {'Content-Type':'application/json'}
'''
proxy  = urllib2.ProxyHandler({'http':'10.199.75.12:8080'})

opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)
'''
req = urllib2.Request(urlladdr, json.dumps(requetdata),headers)

res_data = urllib2.urlopen(req)
res = res_data.read()
print len(res)
#print res
print json.loads(res)