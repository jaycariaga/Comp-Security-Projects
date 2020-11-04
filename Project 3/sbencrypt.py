#!/usr/bin/python3
#Jason Cariaga
#171001720
#done using Python 3.8
# print(x.strip())
# print(x.lstrip() + "braddars")
# print(x.rstrip() + "braddar")

#done using Python 3.8
#attmpt at vencrypt
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
    print(padsize)
    newtxt = msg + chr(padsize).encode() * padsize 
    return newtxt

def swap(block1, block2):
	print("swapping n")


	return newblock;


if sys.version_info < (3, 6) :
    print("This script requires Python version 3.6 or higher")
    sys.exit(1)

#main method starts here
try:
	password = argv[1]
	plainfile = argv[2];
	cipherfile = argv[3];
	#print(key)
except:
	print("please enter in names for password, plaintext, ciphertext");
	exit();

#temp variables instantiated here
prev = None;
kill = 0;

#generating seed - works
seed = sdbm(password)

with open(plainfile, 'rb') as plain_txt:
	with open(cipherfile, 'wb') as ciph_txt:
		while True:
			data = plain_txt.read(16) #comes from plaintext file
			if not data:
				#break;
				if not prev: #if data is actually NULL
					break;
				#if data HAD a previous successful padding:
				if len(prev) < 16: 
					break;
				#when data needs padding and this is last go
				data = pad(data, 16)
				kill = 1; #for when padding done on some space

			#creatingtemp variable repr previous block and without padding
			prev = data; 

			#below handles padding for blocks less than 16 bytes
			if data:			
				data = pad(data, 16)

			# #generating seed - works
			# seed = sdbm(password)
			print(data)

			#setting IV(initialization vector) aka the first 16 bytes of keystream generator - works as far as i know
			congru = seed;
			key = bytearray(b'')
			for i in range(len(data)):
				congru = (1103515245 * congru + 12345) % 256
				print(congru)
				key.append(congru)
			print(key)

			#mybyte is the final ciphertext to append to output file
			mybyte = bytearray(b'')
			for val in range(len(data)): #remember data is limited to 16 byte blocks here!!!
				a = 1103515245
				m = 256
				c = 12345
				if not data: #in case plaintext be empty
					break;

				temp_blk = data[val] ^ key[val]

				result = data[val] ^ congru
				mybyte.append(result);

			#writing time my brothers
			ciph_txt.write(mybyte)
			print(mybyte)

			#kills loop when padding done on some of msg
			if kill:
				break;


plain_txt.close()
ciph_txt.close()

