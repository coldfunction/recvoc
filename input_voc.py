#!/usr/local/bin/python
# -*- coding: UTF-8 -*-
import sys


def input_vocabulary(myfile):
	str='@'
	en = input('Please enter English: \n')
	tw = input('Please enter Chienese: \n')
	entw = en+str+tw
	fid = open(myfile, 'a')
	fid.write(entw)  
	fid.write('\n')  
	fid.close() 
	return entw
