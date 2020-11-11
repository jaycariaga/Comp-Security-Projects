#!/usr/bin/python3
from sys import argv;
import sys;
#Jason Cariaga
#171001720
#done using Python 3.8
import hashlib

try:
	bits = argv[1]
	message = argv[2]
except: 
	print("Please fill in all arguments: [bits] [output]")
	exit()

with open(message, "rb") as msg:
	print ("File: {}".format(message))
	while True:
		data = msg.read()
		if not data:
			break
		#what happens after reading entire file in binary
		m = hashlib.sha256()
		m.update(data)
		computed = m.hexdigest()
		#all works above
		print("Initial-hash: {}".format(computed))
