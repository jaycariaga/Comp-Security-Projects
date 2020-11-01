from sys import argv;
#Jason Cariaga
#171001720
#for reading the keyfile
def read_file(filename):
	with open(filename, "rb") as f:
		data = f.read()
		return data; #currData is binary data of keyfile

def sdbm(input):
	hash = 0;
	for val in input:
		c = input[val]
		hash = c + (hash * (2**6)) + (hash*(2**16)) - hash;
	return hash;

#sample input
x = [0, 1, 2, 3]
#returns bytearray of a series of bytes
mybyte = bytearray(b'')
for val in x:
	a = 1103515245
	m = 256
	c = 12345
	if not x:
		break;
	elif val == 0:
		mybyte.append(x[val])
		continue;
	mybyte.append((a*x[val-1] + c) % m);

print(mybyte)

try:
	password = argv[1]
	plainfile = argv[2];
	cipherfile = argv[3];
	key = read_file(keyfile)
	#print(key)
except:
	print("please enter in names for password, plaintext, ");
	exit();