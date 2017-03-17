#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import httplib,urllib2
import json
from flightValues import *
from datetime import datetime
import time
import re

#间隔时间转换
def queryDateProcess(quryDate):
    '''
    datetime 改为Year-Month-Day
    '''
    dateStr = quryDate[0:4] + '-' + quryDate[4:6] + '-' +quryDate[6:8]
    return dateStr


def floatgetFloatRate(transStr):

	if transStr == '':
		return None
	else:
		if len(re.findall(r'\d+\.\d+', transStr)) == 0:
			if len(re.findall(r'\d+', transStr)) == 0:
				return float(1)
			else:
				return float(re.findall(r'\d+', transStr)[0])/10
		else:
			return float(re.findall(r'\d+\.\d+', transStr)[0])/10



def durationTrans(transStr):

    groupList = re.search(r'(\d+)(.*?)+(\d+)',transStr)

    return groupList.group(1) + 'h' + groupList.group(3) + 'm'



#间隔时间转换
def durationTimeProcess(durationTime):
    '''
    durationTime 将时间间隔格式从HH:MM改为
    HhMm格式
    '''
    timelists = str(durationTime)[0:-3].split(":")
    durationStr = timelists[0]+'h'+timelists[1]+'m'
    return durationStr


#间隔时间转换
def queryDateProcess(quryDate):
    '''
    datetime 改为Year-Month-Day
    '''
    dateStr = quryDate[0:4] + '-' + quryDate[4:6] + '-' +quryDate[6:8]
    return dateStr


#日期转换成星期格式
def tansDateToWeek(dataTime):

    weekDic = {
    1:u"星期一",2:u"星期二",3:u"星期三",
    4:u"星期四",5:u"星期五",6:u"星期六",
    7:u"星期日"
    }
    date_time = datetime.strptime(dataTime, '%Y-%m-%d')
    weekInt = date_time.isoweekday()

    #print weekDic[weekInt]
    return weekDic[weekInt]


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


#http GET请求
def httpGet(urladdr):

    try:
        req = urllib2.Request(urladdr)
        res = urllib2.urlopen(req)
        return res

    except Exception as err:

        print err
        pass


if __name__ == '__main__':
    strs = '2017-03-15'
    tansDateToWeek(strs)