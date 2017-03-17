#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import httplib,urllib2
import json
from flightValues import *
from datetime import datetime
import time
import re
from utility import *

def qunaFlightSegmentsAnalysis(infovalues):
    '''
    jsonValues 为httpPost请求后的数据
    HhMm格式
    '''
    try:
        segmentsList = []
        for i in range(len(infovalues["data"]["flights"])):
            segmentsDic = {}
            pidDic = {}
            baseInfoDic = {}

            #TansPid to string
            pidDic["depArr"] = infovalues["data"]["flights"][i]["shadow"][::-1]
            pidDic["depCity"] = infovalues["data"]["flights"][i]["binfo"]["depCity"]
            pidDic["arrCity"] = infovalues["data"]["flights"][i]["binfo"]["arrCity"]
            pidDic["goDate"] = infovalues["data"]["flights"][i]["binfo"]["depDate"]
            pidDic["flightNo"] = infovalues["data"]["flights"][i]["binfo"]["airCode"]

            segmentsDic["pid"] = json.dumps(pidDic)
            #print type(segmentsDic["pid"])
            baseInfoDic["oraginName"] = pidDic["depCity"]
            baseInfoDic["oragin"] = cityDic[pidDic["depCity"].encode("utf-8")]
            baseInfoDic["destName"] = pidDic["arrCity"]
            baseInfoDic["dest"] = cityDic[pidDic["arrCity"].encode("utf-8")]
            
            #Port information port & PortName
            segmentsDic["depAirport"] = infovalues["data"]["flights"][i]["binfo"]["depAirportCode"]
            segmentsDic["depAirportName"] = infovalues["data"]["flights"][i]["binfo"]["depAirport"]
            segmentsDic["arrAirport"] = infovalues["data"]["flights"][i]["binfo"]["arrAirportCode"]
            segmentsDic["arrAirportName"] = infovalues["data"]["flights"][i]["binfo"]["arrAirport"]

            #depDate & Time & week
            segmentsDic["depDate"] = infovalues["data"]["flights"][i]["binfo"]["depDate"]
            segmentsDic["depTime"] = infovalues["data"]["flights"][i]["binfo"]["depTime"]
            segmentsDic["depWeek"] = tansDateToWeek(infovalues["data"]["flights"][i]["binfo"]["depDate"])

            #arrDate & Time & week
            segmentsDic["arrDate"] = infovalues["data"]["flights"][i]["binfo"]["arrDate"]
            segmentsDic["arrTime"] = infovalues["data"]["flights"][i]["binfo"]["arrTime"]
            segmentsDic["arrWeek"] = tansDateToWeek(infovalues["data"]["flights"][i]["binfo"]["arrDate"])

            #informations
            segmentsDic["carrier"] = infovalues["data"]["flights"][i]["binfo"]["shortCarrier"]
            segmentsDic["carrierName"] = infovalues["data"]["flights"][i]["binfo"]["name"]
            segmentsDic["flightNo"] = infovalues["data"]["flights"][i]["binfo"]["airCode"]
            segmentsDic["duration"] = durationTrans(infovalues["data"]["flights"][i]["binfo"]["flightTime"])
            segmentsDic["airCode"] = infovalues["data"]["flights"][i]["binfo"]["planeFullType"]
            segmentsDic["airCode"] = infovalues["data"]["flights"][i]["binfo"]["planeFullType"]

            segmentsDic["cabinGrade"] = infovalues["data"]["flights"][i]["cabinDesc"]
            segmentsDic["cabin"] = infovalues["data"]["flights"][i]["binfo"]["cabin"]

            #segmentsDic["adultFare"] = float(infovalues["data"]["flights"][i]["minPrice"])
            priceDic = json.loads(infovalues["data"]["flights"][i]["extparams"])
            segmentsDic["adultFare"] = float(priceDic["economyClassMinPrice"])
            segmentsDic["seatCount"] = int(0)
            segmentsDic["stopCity"] = infovalues["data"]["flights"][i]["transCity"]

            if infovalues["data"]["flights"][i]["binfo"]["sellDiscount"] == '0':

                segmentsDic["rate"] = float('%2f'%(float(infovalues["data"]["flights"][i]["binfo"]["bareDiscount"])/10))
            else:
                segmentsDic["rate"] = float('%2f'%(float(infovalues["data"]["flights"][i]["binfo"]["sellDiscount"])/10))

            #Platforms
            segmentsDic["depTerminal"] = infovalues["data"]["flights"][i]["binfo"]["depTerminal"]
            segmentsDic["arrTerminal"] = infovalues["data"]["flights"][i]["binfo"]["arrTerminal"]

            #fontName = infovalues["data"]["flights"][i]["fontName"]

            #print segmentsDic

            segmentsList.append(segmentsDic)

            #print segmentsList

        return segmentsList, baseInfoDic

    except Exception as err:
        print err
        pass




def queryQunaFlightList(queryBody):

    urladdr = urlhub['qunaFlightList']

    resDic = {}

    #try:
    if queryBody['tripType'] == '1':

        queryDic = {"depCity":"","arrCity":"","goDate":"","firstRequest":True,"startNum":"0","sort":"5"}
        queryDic["depCity"] = queryBody['oragin']
        queryDic["arrCity"]   = queryBody['dest']
        queryDic["goDate"]  = queryDateProcess(queryBody['fromDate'])

        res = httpPost(urladdr, queryDic)

        m,n = qunaFlightSegmentsAnalysis(json.loads(res.read()))
        n['cid'] = ""
        n['tripType'] = '1'
        n['fromSegments'] = m
        n['retSegments'] = [{}]

        return n

    elif queryBody['tripType'] == '2':

        queryDic = {"depCity":"","arrCity":"","goDate":"","firstRequest":True,"startNum":"0","sort":"5"}
        queryDic["depCity"] = queryBody['oragin']
        queryDic["arrCity"] = queryBody['dest']
        queryDic["goDate"]  = queryDateProcess(queryBody['fromDate'])

        res = httpPost(urladdr, queryDic)
        m,n = qunaFlightSegmentsAnalysis(json.loads(res.read()))
        n['cid'] = ""
        n['tripType'] = '2'
        n['fromSegments'] = m

        #time.sleep(5)

        queryDic["depCity"] = queryBody['dest']
        queryDic["arrCity"] = queryBody['oragin']
        queryDic["goDate"]  = queryDateProcess(queryBody['retDate'])

        #print requetdata
        resr = httpPost(urladdr, queryDic)
        #print resr.read()
        k,v = qunaFlightSegmentsAnalysis(json.loads(resr.read()))
        
        n['retSegments'] = k

        return n

    else:
        print 'Please put correct parmeter'
        pass

    #except Exception as err:

        #print 'Error id :',err





if __name__ == "__main__":
    '''
    ulladdr = 'https://m.flight.qunar.com/ncs/api/domestic/flightlist'
    postCon = {"depCity":"上海","arrCity":"深圳","goDate":"2017-03-09","firstRequest":True,"startNum":"0","sort":"5"}

    res = httpPost(ulladdr, postCon)

    k,v = qunaFlightSegmentsAnalysis(json.loads(res.read()))

    print k
    '''

    print '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'

    #dicQueryList = {"oragin":"北京","dest":"上海", "tripType":"1","fromDate":"20170320","retDate":"20170325"}
    dicQueryList = {"oragin":"北京","dest":"上海", "tripType":"1","fromDate":"20170320"}

    print queryQunaFlightList(dicQueryList)

