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
	first.update(data) #places data in hash function
	computed = first.hexdigest()
	#print(computed)
	return computed

def getBin (hash):
	binar = bin(int('1'+hash, 16))[3:]
	return binar

def findleadbits(sechash):
	binres = getBin(sechash)
	result = 0
	#print(binres)
	for x in range(len(binres)):
		if not(str(binres[x]) == '0'): #add +1 in [x] for righter bits
			break;
		result += 1
	#print(result)
	return result;

try:
	powheader = argv[1]
	msgfile = argv[2]
except:
	print("please include arguments: [pow-header, original message file]")
	exit()

#storing header data into variables now:
failtest = []
passed = 1
file = ''
inithash = ''
proofwork = ''
nbits = 0
finalhash = ''

with open(powheader, 'r') as pow:
	header = pow.readlines()
	#gets rid of \n
	for line in range(len(header)):
		header[line] = header[line].replace("\n", "")
	for part in header:
		if not part:
			continue
		#print(part)
		arrch = part.split()
		check = arrch[0]
		if "file" in check.lower():
			file = arrch[1]
		if "initial-hash:" in check.lower():
			inithash = arrch[1]
		if "proof-of-work:" in check.lower():
			proofwork = arrch[1]
		if "hash:" in check.lower():
			finalhash = arrch[1]
		if "leading-bits" in check.lower():
			nbits = arrch[1]
	# print(file)
	# print(inithash)
	# print(proofwork)
	# print(nbits)
	#covers first case
	with open(msgfile, 'rb') as msg:
		message = msg.read()
		secmsg = sha256(message)
		if not (secmsg == inithash):
			failtest.append("Test Failed: Message file does NOT hash to the correct value!")

	#checks second case of proof of work
	data = proofwork + secmsg
	hashdata = sha256(data.encode())
	if not (hashdata == finalhash):
		failtest.append("Test Failed: Final Hash of proof of work and file hash string does not match!")
	if not (findleadbits(hashdata) == int(nbits)):
		failtest.append("Test Failed: Leading-bits number does NOT match header's")

	if not failtest:
		print("pass")
	else:
		print('\n'.join(failtest))
