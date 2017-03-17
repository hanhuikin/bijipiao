#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def MainHandler(tornado.web.RequestHandler):
	@tornado.web.asynchronous
	def get(self):
		client = tornado.httpclient.AsyncHTTPClient()
		def callback(response):
			self.write("Hello World")
			self.finish()
		client.fetch("http://www.baidu.com", callback)

		client = tornado.httpclient.AsyncHTTPClient()
		def callback(response):
			self.write("hello World")
			self.finish()
		client.fetch("http://www.baidu.com", callback)

class SleepHandler(tornado.web.RequestHandler):
	@tornado.web.asynchronous
	@tornado.gen.coroutine
	def get(self):
		a = yield tornado.gen.Task(call_subprocess, self, 'sleep 10s')
		print '111', a.read()
		self.write("when i sleep 5s")
		