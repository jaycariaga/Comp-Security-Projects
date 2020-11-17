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
from itertools import permutations

def getBin (hash):
	binar = bin(int('1'+hash, 16))[3:]
	return binar

def checkme(seccomp, checking):
	hashint = int(seccomp, 16)
	#checking = pow(2, 256-nbits)
	if(hashint < checking):
		return True;
	else:
		return False;


def findleadbits(sechash):
	binres = getBin(sechash)
	result = 0
	#print(binres)
	for x in range(len(binres)):
		if not(str(binres[x]) == '0'): #add +1 in [x] for righter bits
			break;
		result += 1
	return result;

#im just gonna leave the character set as globals for sake of O(n)
allchars = string.digits + string.ascii_letters + string.punctuation
allchars = allchars.replace('"', '')
allchars = allchars.replace("'", '')
allchars = allchars.replace(' ', '')

#computed is the first hash, setchars is the tuples, count is iterations starting at 0
def prefixgen(setchars, computed, count, checking, limit):
	for i in setchars:
		proof = ''.join(i)
		tryme = proof + computed
		sechash = hashlib.sha256()
		sechash.update(tryme.encode())
		seccomp = sechash.hexdigest()
		count+=1
		if count > limit:
			print("Too many iterations!!! Stopping execution now:")
			exit()
		if checkme(seccomp, checking):
			return [seccomp, proof, count]
	return 1





limit = 10000000000 #amount of iterations before cutoff saying too much time
count = 0
newlen = 2
try:
	difficulty = int(argv[1])
	message = argv[2]
except: 
	print("Please fill in all arguments: [difficulty] [messagefile]")
	exit()
if difficulty < 0:
	print("Please have difficulty above 0:")
	exit();
elif difficulty > 33:
	newlen = 7
elif difficulty > 30:
	newlen = 6
elif difficulty > 25:
	newlen = 5
elif difficulty > 18:
	newlen = 4
elif difficulty > 17:
	newlen = 3
#setting up permutations based on newlength
# setchars = [''.join(i) for i in permutations(allchars, newlen)]
setchars = permutations(allchars, newlen)

with open(message, "rb") as msg:
	print ("File: {}".format(message))
	while True:
		data = msg.read()
		if not data:
			print("please enter a file with content!")
			break
		#what happens after reading entire file in binary
		first = hashlib.sha256()
		first.update(data) #places data in hash function
		computed = first.hexdigest() #converts message to hash 
		print("Initial-hash: {}".format(computed))
		checking = pow(2, 256-difficulty)

		#start counting time NOW
		start = float(time.time())
		results = prefixgen(setchars, computed, count, checking, limit)
		while results == 1:
			newlen += 1
			setchars = permutations(allchars, newlen)
			results = prefixgen(setchars, computed, count, checking, limit)
		#results = return [seccomp, proof, count]
		timeend = time.time() - start
		print("Proof-of-work: {}".format(results[1]))
		#final hash
		print("Hash: {}".format(results[0]))
		print("Leading-bits: {}".format(findleadbits(results[0])))
		print("Iterations: {}".format(results[2]))
		print("Compute-time: {}".format(timeend))
		exit();

