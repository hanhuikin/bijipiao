#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import PyV8

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
print bsd("2017-03-15", "北京", "上海")


'''
	tansCrypt = execjs.compile("""

	function tans(NumStr, depStr,arrStr){
		var a = "",b = "",c = "", i = "";
		a = NumStr.substr(NumStr.length-1, 1);
		b = depStr.substr(depStr.length-1, 1);
		c = arrStr.substr(arrStr.length-1, 1);
		i = i + a.charCodeAt() + b.charCodeAt() + c.charCodeAt();
		return Number(i).toString(31);
	}
		""")
'''