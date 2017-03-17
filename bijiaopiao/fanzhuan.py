#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import re
import time

s = "ea733a43304e307ca36d4a1b8e8a3e5cd8370171d65f487a97f8c89e785a0e1f571e1a927a30afac14cc3c0cb85bbbc0"
print s[::-1]

ssss = "2.0折"
'''
#pattern = re.compile()
'''
'''
print float(re.findall(r'\d+\.\d+',ssss)[0])
print re.findall(r'\d+',ssss)[0]
print re.findall(r'\d+\s+',ssss)[0]
'''

sd = "10小时50分钟"


def durationTrans(transStr):

    groupList = re.search(r'(\d+)(.*?)+(\d+)',sd)

    return groupList.group(1) + 'h' + groupList.group(3) + 'm'


#print durationTrans(sd)

print float('%2f'%(float('4.4')/10))

#gruoulist = re.search(r'(\d+)([A-Za-z0-9])+(\d+)',sd)

gruoulist = re.search(r'(\d+)(.*?)+(\d+)',sd)



print gruoulist.group(0)
print gruoulist.group(1) + gruoulist.group(3)
print gruoulist.group(2) + gruoulist.group(3)
print gruoulist.group(3)
'''
#print re.search(r'(\d+)([A-Za-z0-9\x80-\xff])+(\d)+',sas).group()
#print re.search(r'(\d+)([A-Za-z0-9\x80-\xff]+)(\d+)',sas).group()

'''
def getFloatRate(transStr):
	if transStr == '':
		return None
	else:
		if len(re.findall(r'\d+\.\d+', transStr)) == 0:
			return float(re.findall(r'\d+', transStr)[0])
		else:
			return float(re.findall(r'\d+\.\d+', transStr)[0])


ssss = "2.1折"
ssrs = "7.0折"
asd = "7折"

print getFloatRate(ssss)
print getFloatRate(ssrs)
print getFloatRate(asd)

