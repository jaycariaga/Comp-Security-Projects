#!/usr/bin/python3
from sys import argv;

#Author: Jason Cariaga
#171001720

try:
	plainfile = argv[2];
	cipherfile = argv[3];
	keyfile = argv[1]
except:
	print("please enter in values for keyfile, plaintext and ciphertext");
	exit();

#reads all contents in bytes and places into an array
bytekey = []
bytetxt = []
with open(keyfile, "rb") as keytxt: #keytxt = open(keyfile, "rb")
		while True:
			byte = keytxt.read(1);
			if not byte:
				break;
			bytekey.append(byte);

with open(plainfile, "rb") as plaintxt: #keytxt = open(keyfile, "rb")
	while True:
		byte = plaintxt.read(1);
		if not byte:
			break;
		bytetxt.append(byte);  

#actually works and covers the case of a null key, and also makes sure to cover repeating keys too
i = 0;
while(len(bytekey) < len(bytetxt)):
	if not bytekey:
		bytekey.append('\0')
	bytekey.append(bytekey[i])
	i += 1;

#converts below to ascii number from 0-255
print(bytetxt)
print(bytekey)
#result = []
result = bytearray(b'')
#to handle encrypting the plaintext and returning the ciphertext
for item in range(len(bytetxt)):
	print(bytetxt[item])
	print(bytekey[item])
	temp = (ord(bytetxt[item]) + ord(bytekey[item % len(bytekey)])) % 256
	result.append(temp)

with open(cipherfile, "wb+") as output:
	#ciphertxt.write(''.join(result))
	print(bytes(result))
	output.write(result)
	#print(str(result))

output.close()
keytxt.close()
