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


def recite_voc():
	fp = open("1_level.txt", "r")
	lines = fp.readlines()
	numOflines = len(lines)
	fp.close()
	
def move_level(src, dst, num):
	fp = open(src, "r")
	lines = fp.readlines()
	length = len(lines)
	move_lines = []

	for i in range(length-1, length-11, -1):
		if i < 0:
			break
		move_lines.append(lines[i])
		print(lines[i])

	length = len(move_lines)
	fp.close()

	fp = open(src, "w")
	for i in range(0, length-10):
		fp.write(lines[i])
	fp.close()
	
	append_lines(move_lines, dst)

	

def recite_voc():
	fp = open("1_level.txt", "r")
	lines = fp.readlines()
	numOflines = len(lines)
	fp.close()
	fp = open("1_level.txt", "w")

	temp_lines = []
	move_lines = []

	if numOflines == 0 :
		#from, to, nums
		move_level("2_level.txt", "1_level.txt", 10)
		recite_voc()

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
	insert_lines(temp_lines, 0, "1_level.txt")
	append_lines(move_lines, "2_level.txt")
	
