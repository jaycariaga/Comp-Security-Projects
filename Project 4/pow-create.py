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

def getBin (hash):
	binar = bin(int('1'+hash, 16))[3:]
	return binar
def checkme(sechash, nbits):
	#res = str("{0:08b}".format(int(sechash, 16)) )
	res = getBin(sechash)
	#print(res)
	for x in range(nbits):
		#print(res[2+x])
		if not(str(res[x]) == '0'): #add +1 in [x] for righter bits
			#print(res[2 + x])
			return False;
	return True;

def findleadbits(sechash):
	binres = getBin(sechash)
	result = 0
	for x in range(len(sechash)):
		result += 1
		if not(str(binres[x]) == '0'): #add +1 in [x] for righter bits
			break;
	return result;


def prefixgen():
	length = random.randint(1,7)
	allchars = string.digits + string.ascii_letters + string.punctuation
	allchars = allchars.replace('"', '')
	allchars = allchars.replace("'", '')
	allchars = allchars.replace(' ', '')
	result = ''.join(random.choice(allchars) for x in range(length))
	#print(result)
	return result


limit = 10000000000 #amount of iterations before cutoff saying too much time
count = 0
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
		#start counting time NOW
		start = float(time.time())
		while True:
			result = prefixgen().encode('ascii') #rand string converted to binary
			#tryme = result + data
			tryme = result.decode() + computed
			#print(tryme)
			sechash = hashlib.sha256()
			sechash.update(tryme.encode())
			seccomp = sechash.hexdigest()
			count+=1
			#print(seccomp)
			if count == limit:
				print("Amount of times eloted")
				exit()
			if checkme(seccomp, difficulty): #if checkme is true, finishes while loop
				timeend = time.time() - start
				proofwork = result.decode()
				print("Proof-of-work: {}".format(proofwork))
				#final hash
				print("Hash: {}".format(seccomp))
				print("Leading-bits: {}".format(findleadbits(seccomp)))
				print("Iterations: {}".format(count))
				print("Compute-time: {}".format(timeend))
				break;

		# res = computed.rjust(difficulty + len(computed), '0') 
		# print(res)

