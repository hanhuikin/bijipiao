# -*- coding: utf-8 -*-
#Author    : hanhuikin
#CreatTime : 2017.01.12
#Vesrin    : V1.0

import os
import logging

def CreatFile(filepath):
	try:
		if os.path.isfile(filepath):
			
			print "File is existed!"

		else:

			fp = open(filepath, 'a+')
			fp.close()

	except Exception as err:

		print err



def logBasicSetting(filepath):
	logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename=filepath,
                filemode='w')
    

    