from sys import argv;
#Author: Jason Cariaga
#171001720
try:
	plainfile = argv[2];
	cipherfile = argv[3];
	keyfile = argv[1]
	#ciphertxt = open(cipherfile)
	keytxt = open(keyfile)
	plaintxt = open(plainfile)
	print(ord('A'))
except:
	print("please enter in values for keyfile, plaintext and ciphertext");
	exit();

bytekey = bytearray(keytxt.read(), 'utf-8')
bytetxt = bytearray(plaintxt.read(), 'utf-8')
print(bytetxt)
print(bytekey)
result = []
#to handle encrypting the plaintext and returning the ciphertext
for item in range(len(bytetxt)):
	print(bytetxt[item])
	#print(bytekey[item])
	temp = (bytetxt[item] + bytekey[item]) % 256
	#print(temp)
	###temp += bytearray(b"A")[0]
	result.append(temp)

ciphertxt = open(cipherfile, "w")
ciphertxt.write(''.join(str(result)))
print(result)

ciphertxt.close()
keytxt.close()


