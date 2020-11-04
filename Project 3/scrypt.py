#!/usr/bin/python3
from sys import argv;
import sys;
#Jason Cariaga
#171001720
#done using Python 3.8

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
#generating seed - works
seed = sdbm(password)
congru = seed;
with open(plainfile, 'rb') as plain_txt:
	with open(cipherfile, 'wb') as ciph_txt:
		while True:
			data = plain_txt.read(1024) #comes from plaintext file
			if not data:
				break;
			# #generating seed - works
			# seed = sdbm(password)

			#returns linear congruential generator
			mybyte = bytearray(b'')
			# congru = seed;
			for val in range(len(data)):
				a = 1103515245
				m = 256
				c = 12345
				if not data:
					break;
				# elif val == 0: #for first case
				# 	result = data[val] ^ ((a*seed+c)%m)
				# 	mybyte.append(result)
				# 	continue;
				congru = (a * congru + c) % m
				#print(congru)
				#congru works, doing xor now
				result = data[val] ^ congru
				#print(result)
				mybyte.append(result);

			#writing time my brothers
			ciph_txt.write(mybyte)
			#print(mybyte)

plain_txt.close()
ciph_txt.close()

