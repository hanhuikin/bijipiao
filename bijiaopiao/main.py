#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import httplib
import urllib2
import urllib
import sys
import cookielib
from valus import *
from bs4 import BeautifulSoup
import csv
import os
import time


def httpPost(urlAddr, postContent):

	headers = {'Content-Type':'application/x-www-form-urlencoded'}

	try:
		
		Data = urllib.urlencode(postContent)

		#proxy  = urllib2.ProxyHandler({'http':'10.199.75.12:8080'})
		#cj     = cookielib.CookieJar()
		#cjopener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
		#urllib2.install_opener(cjopener)

		#opener = urllib2.build_opener(proxy)
		#urllib2.install_opener(opener)
		
		req = urllib2.Request(urlAddr, Data, headers)

		res = urllib2.urlopen(req)
		
		return res

	except Exception as err:

		print err
       



def FlightInfoList(urlladdr, postContent):


	flightList = []
	try:
		response = httpPost(urlladdr, postContent)
		#print response
	
	except Exception as err:
		print err
		return {}

	soup = BeautifulSoup(response.read(), "html.parser")


urlladdr = 'http://m.ctrip.com/html5/flight/flight-list.html?triptype=1&dcode=SZX&acode=SHA&ddate=2017-02-28&seo=0'