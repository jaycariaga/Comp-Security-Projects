#!/usr/bin/python3
#Jason Cariaga
#171001720
#done using Python 3.8
#attmpt at sbdecrypt
from sys import argv;
import sys;

#for reading the file in bytes
def read_file(filename):
	with open(filename, "rb") as f:
		data = f.read()
		return data; #currData is binary data of keyfile

#the S = seed used for ciphertext...WORKS!
def sdbm(input):
	hash = 0;
	for val in input:
		c = ord(val)
		hash = c + (hash * (2**6)) + (hash*(2**16)) - hash;
	return hash;

def pad(msg, size):
    #finds remaining bytes to pad onto
    if not msg:
    	padsize = 16
    else:
    	padsize = (size - len(msg)) % size
    #print(padsize)
    newtxt = msg + chr(padsize).encode() * padsize 
    return newtxt

def swap(result, first, second):
	#print(result)
	temp = result[first]
	result[first] = result[second]
	#print(temp)
	result[second] = temp
	#print(result)
	return result;
	#return newblock;


if sys.version_info < (3, 6) :
    print("This script requires Python version 3.6 or higher")
    sys.exit(1)

#main method starts here
try:
	password = argv[1]
	plainfile = argv[3];
	cipherfile = argv[2];
except:
	print("please enter in names for password, plaintext, ciphertext");
	exit();

#prev stores the previous 16 bytes minus padding; kill var handles final padding; first handles first element case
cipher_tot = []
key = bytearray(b'')
finalres = [] #to be written in plaintext, will be appended in at a time
#generating seed for keystream, key = keystream, and initv is the prev ciphertext block
seed = sdbm(password)
initv = bytearray(b'')
key = bytearray(b'')
current = bytearray(b'')
#to get keystream now
congru = seed
for i in range(16):
	congru = (1103515245 * congru + 12345) % 256
	key.append(congru)
key = key[0:16]

#starting to read cipherfile and plaintext for writing below
with open(cipherfile, 'rb') as ciph_txt:
	with open(plainfile, 'wb') as plain_txt:
		while True:
			data = ciph_txt.read(16) #comes from plaintext file
			if not data:
				break;
			cipher_tot.append(bytearray(data))
			#print(data)

		#i will be xoring the keystream key and the read 16 byte data and insert to the temporary cipher_tot
		for i in range(len(cipher_tot)): #browses a block a time
			current = cipher_tot[-i-1]
			#print(current)
			count = 0
			temp = bytearray(b'')
			for j in current: #should browse all bytes of each block
				#trying to xor starting from the last element 
				temp.append(j ^ key[count])
				count += 1
			current = temp

			#this should be the keystream swap going back in
			for k in range(16):
				first = key[k] & 0xf
				second = (key[k] >> 4) & 0xf
				current = swap(current, first, second)
			print(-i-1)
			cipher_tot[-i-1] = current
			if(i == len(cipher_tot) - 1):
				for k in range(16):
					current[k] = current[k] ^ key[k]
				cipher_tot[0] = current
				break;
			else:
				for k in range(16):
					current[k] = current[k] ^ cipher_tot[-i-2][k]

		for val in cipher_tot:
			plain_txt.write(val)


		#print(cipher_tot)

		#this for loop will cover handling blocks from end to start by decrementation
		# for i in range(len(cipher_tot)):
		# 	cipher_tot[i] = cipher_tot[i][0:16] ^ key[0:16]
			#print(cipher_tot[-i]) #how to access in reverse form

plain_txt.close()
ciph_txt.close()

