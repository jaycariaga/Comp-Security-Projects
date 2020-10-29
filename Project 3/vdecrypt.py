from sys import argv;
#Author: Jason Cariaga
#171001720
try:
	plainfile = argv[3];
	cipherfile = argv[2];
	keyfile = argv[1]
	#keytxt = open(keyfile, "rb") 
	# #plaintxt = open(plainfile, "rb")
except:
	print("please enter in values for keyfile, plaintext and ciphertext");
	exit();

#reads all contents in bytes and places into an array
bytekey = []
bytetxt = []
byteciph = []
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

# with open(cipherfile, "rb") as ciphertxt: #keytxt = open(keyfile, "rb")
# 	while True:
# 		byte = ciphertxt.read(1);
# 		if not byte:
# 			break;
# 		byteciph.append(byte);  
ciphertxt = open(cipherfile, encoding="utf-8")
byteciph = bytearray(ciphertxt.read(), 'utf-8')
	#plaintxt = open(plainfile, "rb")

#actually works and covers the case of a null key, and also makes sure to cover repeating keys too
i = 0;
while(len(bytekey) < len(bytetxt)):
	if not bytekey:
		bytekey.append('\0')
	bytekey.append(bytekey[i])
	i += 1;

print(bytekey)
print(byteciph)