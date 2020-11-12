#!/usr/bin/python3
from sys import argv;
import sys;
#Jason Cariaga
#171001720
#done using Python 3.8
import hashlib
import random
import string


def checkme(sechash, nbits):
	res = ''.join(format(ord(i), 'b') for i in sechash) 
	print(res)
	for x in range(nbits):
		if not(str(res[x]) == '0'):
			print(res[x])
			#return True;
	return True;


def prefixgen():
	length = random.randint(1,7)
	allchars = string.digits + string.ascii_letters + string.punctuation
	allchars = allchars.replace('"', '')
	allchars = allchars.replace("'", '')
	allchars = allchars.replace(' ', '')
	result = ''.join(random.choice(allchars) for x in range(length))
	return result


limit = 10000000000 #amount of iterations before cutoff saying too much time
current = 0
try:
	difficulty = int(argv[1])
	message = argv[2]
except: 
	print("Please fill in all arguments: [difficulty] [messagefile]")
	exit()
if difficulty < 0:
	print("Please have difficulty above 0:")
	exit();

with open(message, "rb") as msg:
	print ("File: {}".format(message))
	while True:
		data = msg.read()
		if not data:
			break
		#what happens after reading entire file in binary
		first = hashlib.sha256()
		first.update(data) #places data in hash function
		computed = first.hexdigest() #converts message to hash 
		#all works above
		print("Initial-hash: {}".format(computed))

		while True:
			result = prefixgen().encode('ascii') #rand string converted to binary
			tryme = result + data
			sechash = hashlib.sha256()
			sechash.update(tryme)
			seccomp = sechash.hexdigest()
			print(seccomp)
			if checkme(seccomp, difficulty): #if checkme is true, finishes while loop
				print("sechash is: {}".format(seccomp))
				print("computed is: {}".format(computed))
				break;

		# res = computed.rjust(difficulty + len(computed), '0') 
		# print(res)

