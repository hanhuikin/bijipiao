#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import httplib,urllib2,urllib
import json
from flightValues import *
from bs4 import BeautifulSoup as bs
from utility import *
#import execjs
import PyV8



def quanFlightDetail(queryDic):

	refundChangDic = {}

	try:
		urladd = urlhub['quanFligthDetail'] + urllib.urlencode(queryDic)
		#print urladd

		req = urllib2.Request(urladd, headers = header)
		h5Page = urllib2.urlopen(req)
		soup = bs(h5Page.read(), "html.parser")

		#print soup

		contentDic = soup.li.attrs

		refundChangDic["wrapperId"] = contentDic["data-wrapper-id"]
		refundChangDic["domain"] = contentDic["data-domain"]
		refundChangDic["policyId"] = contentDic["data-policyid"]

		refundChangDic["index"] = contentDic["data-index"]
		refundChangDic["flightNo"] = contentDic["data-flight-no"]
		refundChangDic["realFlightKey"] = ""

		refundChangDic["flightType"] = contentDic["data-flight-type"]
		refundChangDic["depDate"] = contentDic["data-dep-date"]
		refundChangDic["retDate"] = ""

		refundChangDic["depTime"] = contentDic["data-dep-time"]
		refundChangDic["depAirport"] = contentDic["data-dep-airport"]
		refundChangDic["arrAirport"] = contentDic["data-arr-airport"]
		refundChangDic["extInfo"] = contentDic["data-ext-info"]

		refundChangDic["isInter"] = contentDic["data-is-inter"]

		return refundChangDic

	except Exception as err:

		print 'err is ',err
		pass







def quanRefundChangAnalysis(requestDic):

	resRefundChang = {}

	urladdrs = urlhub['quanH5FlightInfo']
	try:
		data = urllib.urlencode(requestDic)
		req = urllib2.Request(urladdrs, data, header)
		res = urllib2.urlopen(req)

		resDic = json.loads(res.read())

		refundList = (resDic['tips'][0]['items'][0]['content']['value']).split('\n')
		
		if len(refundList) == 0:
			resRefundChang['ifRefund'] = None
			resRefundChang['refundFeeBefore'] = None
			resRefundChang['refundFeeAfter'] = None
		elif len(refundList) == 1:
			resRefundChang['ifRefund'] = False
			resRefundChang['refundFeeBefore'] = ''
			resRefundChang['refundFeeAfter'] = ''
		else:
			resRefundChang['ifRefund'] = True
			resRefundChang['refundFeeBefore'] = refundList[0]
			resRefundChang['refundFeeAfter'] = refundList[1]

		changeList = (resDic['tips'][0]['items'][1]['content']['value']).split('\n')
		
		if len(changeList) == 0:
			resRefundChang['ifChange'] = None
			resRefundChang['changeFeeBefore'] = None
			resRefundChang['changeFeeAfter'] = None
		elif len(changeList) == 1:
			resRefundChang['ifChange'] = False
			resRefundChang['changeFeeBefore'] = ''
			resRefundChang['changeFeeAfter'] = ''
		else:
			resRefundChang['ifChange'] = True
			resRefundChang['changeFeeBefore'] = changeList[0]
			resRefundChang['changeFeeAfter'] = changeList[1]

		endorsementList = (resDic['tips'][0]['items'][2]['content']['value']).split('\n')
		
		if len(endorsementList) == 0:
			resRefundChang['ifEndorsement'] = None
			resRefundChang['endorseMsg'] = None
		elif len(endorsementList) == 1:
			resRefundChang['ifEndorsement'] = False
			resRefundChang['endorseMsg'] = endorsementList[0]
		else:
			resRefundChang['ifEndorsement'] = True
			resRefundChang['endorseMsg'] = endorsementList[0]

		resRefundChang['remark'] = resDic['tips'][0]['items'][3]['content']['value']

		return resRefundChang


	except Exception as err:
		print "err is:", err
		return {}




def queryQunaRefundChangList(queryBody):

	ctxt = PyV8.JSContext()
	ctxt.enter()
	func = ctxt.eval('''function tans(NumStr, depStr,arrStr){
			var a = "",b = "",c = "", i = "";
			a = NumStr.substr(NumStr.length-1, 1);
			b = depStr.substr(depStr.length-1, 1);
			c = arrStr.substr(arrStr.length-1, 1);
			i = i + a.charCodeAt() + b.charCodeAt() + c.charCodeAt();
			return Number(i).toString(31);}''')

	bsd = ctxt.locals.tans
	
	dDepArr = bsd(queryBody["pid"]["goDate"], queryBody["pid"]["depCity"], queryBody["pid"]["arrCity"])

	#print 'dDepArr',dDepArr

	try:
		postQunaDic = {"startCity":queryBody["pid"]["depCity"].encode("utf-8"),
		 "destCity":queryBody["pid"]["arrCity"].encode("utf-8"),
		 "startDate":queryBody["pid"]["goDate"],
		 "flightType":"oneWay",
		 "transferCity":"",
		 "transfer":"0",
		 "from":"",
		 "code":queryBody["pid"]["flightNo"],
		 }
		
		postQunaDic[dDepArr] = queryBody["pid"]["depArr"]

		#print 'postQunaDic',postQunaDic


		return quanRefundChangAnalysis(quanFlightDetail(postQunaDic))

	except Exception as err:
		print err
		return {}


if __name__ == "__main__":
	from sequna import *

	postCon = {"depCity":"北京","arrCity":"上海","goDate":"2017-03-16","firstRequest":True,"startNum":"0","sort":"5"}
	urladdr = urlhub['qunaFlightList']

	res = httpPost(urladdr, postCon)

	k,v = qunaFlightSegmentsAnalysis(json.loads(res.read()))

	print k[0]["pid"]

	dicTest = {"pid":{"depCity":k[0]["pid"]["depCity"],
	"arrCity":k[0]["pid"]["arrCity"],
	"goDate":k[0]["pid"]["goDate"],
	"flightNo":k[0]["flightNo"],
	"depArr":k[0]["pid"]["depArr"]
	},"cid":""}

	#print dicTest

	print queryQunaRefundChangList(dicTest)


	'''
	dDepArr = tansCrypt.call("tans", postCon["goDate"], postCon["depCity"], postCon["arrCity"])

	postQunaDic = {"startCity":postCon["depCity"],
	 "destCity":postCon["arrCity"],
	 "startDate":postCon["goDate"],
	 "flightType":"oneWay",
	 "transferCity":"",
	 "transfer":"0",
	 "from":"",
	 "code":k[0]["flightNo"],
	 }
	postQunaDic[dDepArr] = k[0]["pid"]

	print quanRefundChangAnalysis(quanFlightDetail(postQunaDic))
'''