#!/usr/local/bin/python
# -*- coding: UTF-8 -*-
import sys


def input_vocabulary():
	str='@'
	en = input('Please enter English: \n')
	tw = input('Please enter Chienese: \n')
	entw = en+str+tw
	fid = open('1_level.txt', 'a')
	fid.write(entw)  
	fid.write('\n')  
	fid.close() 
	return entw

#entw = input_vocabulary()
#print(entw)

#fid = open('test.txt', 'a')  
#fid.write(entw)  
#fid.write('\n')  
#fid.close() 
