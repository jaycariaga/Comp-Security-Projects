from sys import argv;
#Author: Jason Cariaga
#171001720
try:
	plainfile = argv[2];
	cipherfile = argv[3];
	keyfile = argv[1]
	#keytxt = open(keyfile, "rb") 
	# #plaintxt = open(plainfile, "rb")
except:
	print("please enter in values for keyfile, plaintext and ciphertext");
	exit();


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
	#plaintxt = open(plainfile, "rb")

#actually works and covers the case of a null key LMAO
while(len(bytekey) < len(bytetxt)):
	i = 0;
	if not bytekey:
		bytekey.append('\0')
	bytekey.append(bytekey[i])
	i += 1;

#converts below to ascii number from 0-255

#bytekey = bytearray(keytxt.read(), 'utf-8')
#bytetxt = bytearray(plaintxt.read(), 'utf-8')
print(bytetxt)
print(bytekey)
result = []
#to handle encrypting the plaintext and returning the ciphertext
try:
	for item in range(len(bytekey)):
		print(bytetxt[item])
		print(bytekey[item])
		temp = (ord(bytetxt[item]) + ord(bytekey[item])) % 256
		#print(temp)
		result.append(temp)
except:
	print("please have the correct length between keyfile and plaintext");
	exit();

ciphertxt = open(cipherfile, "w")
# ciphertxt.write(''.join(str(result)))
ciphertxt.write(str(result))
print(str(result))

ciphertxt.close()
keytxt.close()


