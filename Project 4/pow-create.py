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
# def checkme(sechash, nbits):
# 	#res = str("{0:08b}".format(int(sechash, 16)) )
# 	res = getBin(sechash)
# 	print(res)
# 	for x in range(nbits):
# 		#print(res[2+x])
# 		if not(str(res[x]) == '0'): #add +1 in [x] for righter bits
# 			#print(res[2 + x])
# 			return False;
# 	return True;
#validity check done via math instead of for loop for better O(n)
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
def prefixgen(newlen):
	length = random.randint(newlen,8)
	result = ''.join(random.choice(allchars) for x in range(length))
	#print(result)
	return result


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
elif difficulty > 30:
	newlen = 6
elif difficulty > 25:
	newlen = 5
elif difficulty > 18:
	newlen = 4
elif difficulty > 17:
	newlen = 3
try:
	f = open(message, 'r')
except:
	print("Invalid file! Try again")
	exit()
f.close()
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
		while count < limit:
			result = prefixgen(newlen).encode('ascii') #rand string converted to binary
			#tryme = result + data
			tryme = result.decode() + computed
			#print(tryme)
			sechash = hashlib.sha256()
			sechash.update(tryme.encode())
			seccomp = sechash.hexdigest()
			count+=1

			if checkme(seccomp, checking): #if checkme is true, finishes while loop
				timeend = time.time() - start
				proofwork = result.decode()
				print("Proof-of-work: {}".format(proofwork))
				#final hash
				print("Hash: {}".format(seccomp))
				print("Leading-bits: {}".format(findleadbits(seccomp)))
				print("Iterations: {}".format(count))
				print("Compute-time: {}".format(timeend))
				exit();
		print("Too many iterations! Stopping execution now.")
		exit()


