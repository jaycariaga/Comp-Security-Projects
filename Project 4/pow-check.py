#!/usr/bin/python3
from sys import argv;
import sys;
#Jason Cariaga
#171001720
#done using Python 3.8
import hashlib
import random
import string
import time


def sha256(data):
	#remember that data in update must be binary
	first = hashlib.sha256()
	first.update(data.encode()) #places data in hash function
	computed = first.hexdigest()
	print(computed)
	return computed


try:
	powheader = argv[1]
	file = argv[2]
except:
	print("please include arguments: [pow-header, original message file]")
	exit()

#storing header data into variables now:
file = ''
inithash = ''
proofwork = ''
nbits = 0

with open(powheader, 'r') as pow:
	header = pow.readlines()
	#gets rid of \n
	for line in range(len(header)):
		header[line] = header[line].replace("\n", "")
	file = (header[0].split())[1]
	inithash = (header[1].split())[1]
	proofwork = (header[2].split())[1]
	nbits = (header[4].split())[1]
	data = proofwork + inithash
	print(data)
	sha256(data)