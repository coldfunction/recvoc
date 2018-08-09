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
	

def recite_voc():
	fp = open("1_level.txt", "r")
	lines = fp.readlines()
	numOflines = len(lines)
	fp.close()
	fp = open("1_level.txt", "w")

	temp_lines = []
	move_lines = []
	for line in lines:
		os.system('clear')
		print("numof lines ", numOflines)
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
	
