#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import httplib
import urllib2
import urllib
import sys
import cookielib
from bs4 import BeautifulSoup
import csv
import os
import time

refundChangDic = {}
soup = BeautifulSoup(open('sequna.html'), "html.parser")

contentDic = soup.li.attrs

refundChangDic["wrapperId"] = contentDic["data-wrapper-id"]
refundChangDic["domain"] = contentDic["data-domain"]
refundChangDic["policyId"] = contentDic["data-policyid"]
refundChangDic["index"] = contentDic["data-index"]
refundChangDic["flightNo"] = contentDic["data-flight-no"]
refundChangDic["realFlightKey"] = ''
refundChangDic["flightType"] = contentDic["data-flight-type"]
refundChangDic["depDate"] = contentDic["data-dep-date"]
refundChangDic["retDate"] = contentDic["data-ret-date"]
refundChangDic["depTime"] = contentDic["data-dep-time"]
refundChangDic["depAirport"] = contentDic["data-dep-airport"]
refundChangDic["arrAirport"] = contentDic["data-arr-airport"]
refundChangDic["extInfo"] = contentDic["data-ext-info"]
refundChangDic["isInter"] = contentDic["data-is-inter"]


print refundChangDic

