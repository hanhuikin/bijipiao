#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import re
import time
import sys
import math

import execjs

print sys.getdefaultencoding()
cd = []
ss = "0京海"
tans = ss.decode('utf-8')
#print tans
strs = ''
for i in range(len(tans)):

	strs = strs + str(ord(tans[i]))
	print strs
print strs


#print int(str(int(strs)),31)

'''
cd.append(ss)
cc = ss.decode('UTF-8') 

cd.append(cc)
print cd

print str(ord('0'))+str(ord(cc))
'''

ctx=execjs.compile("""

		function add(x, y){
		return x+y
		}

		""")

print ctx.call("add",1,2)


tansCrypt = execjs.compile("""

function tans(NumStr, depStr,arrStr){
	var a = "",b = "",c = "", i = "";
	a = NumStr.substr(NumStr.length-1, 1);
	console.log(a)
	b = depStr.substr(depStr.length-1, 1);
	c = arrStr.substr(arrStr.length-1, 1);
	i = i + a.charCodeAt() + b.charCodeAt() + c.charCodeAt();
	return Number(i).toString(31);
}


	""")

print tansCrypt.call("tans", "2017-03-15", "北京", "上海")