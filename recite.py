#!/usr/local/bin/python
# -*- coding: UTF-8 -*-
import sys
import os

def append_lines(lines, myfile):
	f = open(myfile, "a")
	for line in lines:
		f.write(line)	
	f.close()

def insert_lines(lines, pos, myfile):
	if not lines:
		f = open(myfile, "w")
		f.close()
	for line in lines:
		insert_line(0, line, myfile)

def insert_line(index, line, myfile):
	f = open(myfile, "r")
	contents = f.readlines()
	f.close()

	contents.insert(index, line)
	f = open(myfile, "w")
	contents = "".join(contents)
	f.write(contents)
	f.close()
	
def move_level(src, dst, num):
	fp = open(src, "r")
	lines = fp.readlines()
	length = len(lines)
	move_lines = []

	for i in range(0, num):
		if i > length-1:
			break
		move_lines.append(lines[i])

	fp.close()

	fp = open(src, "w")
	for i in range(num, length):
		fp.write(lines[i])
	fp.close()
	
	append_lines(move_lines, dst)
	

def recite_voc(f_level1, f_level2):
	fp = open(f_level1, "r")
	lines = fp.readlines()
	numOflines = len(lines)
	fp.close()

	temp_lines = []
	move_lines = []

	if numOflines == 0 :
		fpp = open(f_level2, "r")
		nlines = fpp.readlines()
		if len(nlines) == 0:
			print("Please insert new voc!!\n")
			fpp.close()
			return False
		fpp.close()
		#from, to, nums
		move_level(f_level2, f_level1, 10)
		return recite_voc(f_level1, f_level2)
		
	fp = open(f_level1, "w")

	for line in lines:
		os.system('clear')
		myvoc = line.split("@")
		print(myvoc[0])
		input('answer: \n')
		print(myvoc[1])
		op = input('Is correct in your mind? (y/n)')
		if op == 'n':
			temp_lines.append(line)
			print("yes it should move forward")
		else:
			move_lines.append(line)
			print("yes it should move out")
	fp.close()
	
	insert_lines(temp_lines, 0, f_level1)
	append_lines(move_lines, f_level2)
	return True

