#!/usr/bin/python3
#Jason Cariaga
#171001720
#done using Python 3.8
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
	plainfile = argv[2];
	cipherfile = argv[3];
except:
	print("please enter in names for password, plaintext, ciphertext");
	exit();

#prev stores the previous 16 bytes minus padding; kill var handles final padding; first handles first element case
prev = None;
kill = 0;
first = 1;

#generating seed for keystream, key = keystream, and initv is the prev ciphertext block
seed = sdbm(password)
initv = bytearray(b'')
key = bytearray(b'')
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
			#print(data)

			#setting IV(initialization vector) aka the first 16 bytes of keystream generator - works as far as i know
			congru = seed;

			#keystream generator for first 16 bytes of key
			if first:
				for i in range(len(data)):
					congru = (1103515245 * congru + 12345) % 256
					key.append(congru)
				key = key[0:16]
				initv = key
				first = 0;

			#mybyte is the temp block for final xor after the for loop
			mybyte = bytearray(b'')
			final = bytearray(b'')
			#xor'ing vector and plaintext bytes below:
			for val in range(len(data)): #remember data is limited to 16 byte blocks here!!!
				if not data: #in case plaintext be empty
					break;
				temp_blk = data[val] ^ initv[val]
				mybyte.append(temp_blk);
			#swapping keystream bytes for xor
			print(mybyte)
			for i in range(16):
				first = key[i] & 0xf
				second = (key[i] >> 4) & 0xf
				mybyte = swap(mybyte, first, second)

			#key = swap(key)
			
			for i in range(16):
				final.append( mybyte[i] ^ key[i] );

			initv = final
			#writing time my brothers
			ciph_txt.write(final)
			#print(mybyte)
			#print(final)

			#kills loop when padding done on some of msg
			if kill:
				break;


plain_txt.close()
ciph_txt.close()

