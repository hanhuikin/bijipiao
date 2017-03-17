#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import httplib, ssl, urllib2, socket
import json
from flightValues import *
from datetime import datetime
import time
from utility import *


#Segmeng信息解析处理
def flightSegmentsAnalysis(infovalues):
    '''
    jsonValues 为httpPost请求后的数据
    HhMm格式
    '''
    #segmentsDic = {}
    #baseInfoDic = {}

    try:
        segmentsList = []
        for i in range(len(infovalues['fltitem'])):
            
            for k in range(len(infovalues['fltitem'][i]['mutilstn'])):
                segmentsDic = {}
                baseInfoDic = {}

                #fligthNo is Number need process
                #flightNo and carrier 
                segmentsDic["flightNo"] = infovalues['fltitem'][i]['mutilstn'][k]['basinfo']['flgno']
                segmentsDic["carrier"] = infovalues['fltitem'][i]['mutilstn'][k]['basinfo']['aircode']
                segmentsDic["carrierName"] = infovalues['fltitem'][i]['mutilstn'][k]['basinfo']['airsname']
                #print 'airsname:',infovalues['fltitem'][i]['mutilstn'][k]['basinfo']['airsname']

                #baseInfoDic include the city & cityName
                baseInfoDic["oragin"] = infovalues['fltitem'][i]['mutilstn'][k]['dportinfo']['city']
                baseInfoDic["oraginName"] = infovalues['fltitem'][i]['mutilstn'][k]['dportinfo']['cityname']
                baseInfoDic["dest"] = infovalues['fltitem'][i]['mutilstn'][k]['aportinfo']['city']
                baseInfoDic["destName"] = infovalues['fltitem'][i]['mutilstn'][k]['aportinfo']['cityname']

                #Port information port & PortName
                segmentsDic["depAirport"] = infovalues['fltitem'][i]['mutilstn'][k]['dportinfo']['aport']
                segmentsDic["depAirportName"] = infovalues['fltitem'][i]['mutilstn'][k]['dportinfo']['aportsname']
                segmentsDic["arrAirport"] = infovalues['fltitem'][i]['mutilstn'][k]['aportinfo']['aport']
                segmentsDic["arrAirportName"] = infovalues['fltitem'][i]['mutilstn'][k]['aportinfo']['aportsname']

                #Platform Name
                segmentsDic["depTerminal"] = infovalues['fltitem'][i]['mutilstn'][k]['dportinfo']['bsname']
                segmentsDic["arrTerminal"] = infovalues['fltitem'][i]['mutilstn'][k]['aportinfo']['bsname']

                #DateInformation
                depDateTime = infovalues['fltitem'][i]['mutilstn'][k]['dateinfo']['ddate']
                depDateTimeList = depDateTime.split(" ")
                segmentsDic["depDate"] = depDateTimeList[0]
                segmentsDic["depTime"] = depDateTimeList[1][0:-3]
                segmentsDic["depWeek"] = infovalues['fltitem'][i]['mutilstn'][k]['dateinfo']['dweek']

                arrDateTime = infovalues['fltitem'][i]['mutilstn'][k]['dateinfo']['adate']
                arrDateTimeList = arrDateTime.split(" ")
                segmentsDic["arrDate"] = arrDateTimeList[0]
                segmentsDic["arrTime"] = arrDateTimeList[1][0:-3]
                segmentsDic["arrWeek"] = infovalues['fltitem'][i]['mutilstn'][k]['dateinfo']['aweek']

                durationTime = datetime.strptime(arrDateTime, '%Y-%m-%d %H:%M:%S') - datetime.strptime(depDateTime, '%Y-%m-%d %H:%M:%S')
                segmentsDic["duration"] = durationTimeProcess(durationTime)
                segmentsDic["airCode"] = infovalues['fltitem'][i]['mutilstn'][k]['craftinfo']['cname']

                #maybe the list be null
                if len(infovalues['fltitem'][i]['mutilstn'][k]['fsitem']) == 0:
                    segmentsDic["stopCity"] = ''
                else:
                    segmentsDic["stopCity"] = infovalues['fltitem'][i]['mutilstn'][k]['fsitem'][0]["city"]

                #for j in range(len(infovalues['fltitem'][i]['policyinfo'])):
                policyInfoDic = {}
                #print '#############################################################',policyInfoDic
                policyInfoDic["pid"] = infovalues['fltitem'][i]['policyinfo'][0]['pid']
                policyInfoDic["adultFare"] = float(infovalues['fltitem'][i]['policyinfo'][0]['tprice'])
                policyInfoDic["seatCount"] = int(infovalues['fltitem'][i]['policyinfo'][0]['quantity'])
                policyInfoDic["rate"] = float(infovalues['fltitem'][i]['policyinfo'][0]['drate'])
                policyInfoDic["cabinGrade"] = infovalues['fltitem'][i]['policyinfo'][0]['classinfor'][0]['display']
                policyInfoDic["cabin"] = infovalues['fltitem'][i]['policyinfo'][0]['classinfor'][0]['sclass']
                #segmentsList.append(policyInfoDic.update(segmentsDic))
                policyInfoDic.update(segmentsDic)
                #print policyInfoDic
                segmentsList.append(policyInfoDic)

        return segmentsList, baseInfoDic

    except Exception as err:

        print "*******************"
        print err
        print "*******************"
        pass



def genCid():
    
    try:
        
        res = httpGet(urlhub['ClientID'])

        resDic = json.loads(res.read())
        
        print resDic['ClientID']
        return resDic['ClientID']
        
        #return '09031015111609068709'


    except Exception as err:
        
        return None



def queryFlightList(queryBody):

    clientID = genCid()
    urladdr  = urlhub['Segments'] + clientID
    #print urladdr

    try:

        if queryBody['tripType'] == '1':

            queryList = [{"dccode":None,"accode":None,"dtime":None}]
            
            queryList[0]["dccode"] = queryBody['oragin']
            queryList[0]["accode"]   = queryBody['dest']
            queryList[0]["dtime"]  = queryDateProcess(queryBody['fromDate'])
            requestFlightdata["searchitem"]  = queryList
            requestFlightdata["head"]["cid"] = clientID

            res = httpPost(urladdr, requestFlightdata)
            #print '++++++++++++'
            #print res
            m,n = flightSegmentsAnalysis(json.loads(res.read()))
            n['cid'] = clientID
            n['tripType'] = '1'
            n['fromSegments'] = m
            n['retSegments'] = [{}]

            return n

        elif queryBody['tripType'] == '2':

            queryList = [{"dccode":None,"accode":None,"dtime":None}]
            queryList[0]["dccode"] = queryBody['oragin']
            queryList[0]["accode"] = queryBody['dest']
            queryList[0]["dtime"] = queryDateProcess(queryBody['fromDate'])

            requestFlightdata["searchitem"]  = queryList
            requestFlightdata["head"]["cid"] = clientID

            res = httpPost(urladdr, requestFlightdata)
            m,n = flightSegmentsAnalysis(json.loads(res.read()))
            n['cid'] = clientID
            n['tripType'] = '2'
            n['fromSegments'] = m

            #time.sleep(5)

            queryList[0]["dccode"] = queryBody['dest']
            queryList[0]["accode"] = queryBody['oragin']
            queryList[0]["dtime"] = queryDateProcess(queryBody['retDate'])

            requestFlightdata["searchitem"]  = queryList
            #print requetdata
            resr = httpPost(urladdr, requestFlightdata)
            #print resr.read()
            k,v = flightSegmentsAnalysis(json.loads(resr.read()))
            
            n['retSegments'] = k

            return n

        else:
            print 'Please put correct parmeter'

    except Exception as err:

        print "*******************"
        print err
        print "*******************"
        pass



def refundChangeAnalysis(PolicyValues,clientID):
    
    resRefundChang = {}
    try:
        urladdr = urlhub['Refund'] + clientID
        print urladdr
        if len(PolicyValues["policylist"]) != 0:
            pid = PolicyValues["policylist"][0]["pid"]
            requestRefundChangeData["prpid"] = pid
            requestRefundChangeData["head"]["cid"] = clientID
            res = httpPost(urladdr, requestRefundChangeData)

            refundChangDic = json.loads(res.read())
            #print refundChangDic

            RefundList = refundChangDic['segnotes'][0]['notes'][2]['tables'][0]['content'][0]["subcontent"]
            
            if len(RefundList) == 0:
                print 'Can not find the node'
                resRefundChang['ifRefund'] = None
                resRefundChang['refundFeeBefore'] = None
                resRefundChang['refundFeeAfter'] = None
            elif len(RefundList) == 1:
                resRefundChang['ifRefund'] = False
                resRefundChang['refundFeeBefore'] = ''
                resRefundChang['refundFeeAfter'] = ''
            else:
                resRefundChang['ifRefund'] = True
                resRefundChang['refundFeeBefore'] = RefundList[0]
                resRefundChang['refundFeeAfter'] = RefundList[1]

            changeList = refundChangDic['segnotes'][0]['notes'][2]['tables'][1]['content'][0]["subcontent"]

            if len(changeList) == 0:
                print 'Can not find the node'
                resRefundChang['ifChange'] = None
                resRefundChang['changeFeeBefore'] = None
                resRefundChang['changeFeeAfter'] = None
            elif len(changeList) == 1:
                resRefundChang['ifChange'] = False
                resRefundChang['changeFeeBefore'] = ''
                resRefundChang['changeFeeAfter'] = ''
            else:
                resRefundChang['ifChange'] = True
                resRefundChang['changeFeeBefore'] = RefundList[0]
                resRefundChang['changeFeeAfter'] = RefundList[1]

            endorsementList = refundChangDic['segnotes'][0]['notes'][2]['tables'][2]['content'][0]["subcontent"]

            if len(endorsementList) == 0:
                print 'Can not find the node'
                resRefundChang['ifEndorsement'] = None
                resRefundChang['endorseMsg'] = None
            elif len(endorsementList) == 1:
                resRefundChang['ifEndorsement'] = False
                resRefundChang['endorseMsg'] = endorsementList[0]
            else:
                resRefundChang['ifEndorsement'] = True
                resRefundChang['endorseMsg'] = endorsementList[0]

            extraList = refundChangDic['segnotes'][0]['notes'][2]['tables'][3]['extra']

            extra = ''

            for i in range(len(extraList)):

                extra = extra + ','+ extraList[i]

            resRefundChang['remark'] = extra
        
            #print resRefundChang
            return resRefundChang

        else:

            return ''

    except Exception as err:
        print err
        pass






def queryRefundChange(queryBody):

    try:

        cid = queryBody['cid']

        urladdr = urlhub['PolicyList'] + cid
        requestPolicyListData["prdid"] = queryBody['pid']
        requestPolicyListData["head"]["cid"] = cid

        res = httpPost(urladdr, requestPolicyListData)

        respose = refundChangeAnalysis(json.loads(res.read()),cid)

        print respose

        return respose

    except Exception as err:

        print '##################'
        print err
        pass







if __name__ == "__main__":

    dicss = {"oragin":"BJS","dest":"SHA", "tripType":"2","fromDate":"20170310","retDate":"20170312"}
    dicsss = {"oragin":"SHA","dest":"BJS", "tripType":"1","fromDate":"20170319"}
    print queryFlightList(dicsss)

    policyDic = {'cid':'09031160411041447304','pid':'owGwCqABeyJmbm8iOiJLTjU5ODciLCJkZGF0ZSI6IjIwMTctMy05IDIxOjU1OjAwARw0Y2l0eSI6IkJKUyIsImENDlBTSEEiLCJwcmljZSI6MC4wLCJ3ZXcNCgB0LhcAAHYBPbgwLCJ0aWQiOiIwNjdhNjcwZS04ZDgwLTQ5NjgtYjVmZS05MjRjOGUzZjEwN2EifQ=='}

    #print queryRefundChange(policyDic)
