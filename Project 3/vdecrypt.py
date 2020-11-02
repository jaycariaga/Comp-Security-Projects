#Jason Cariaga
#171001720
#done using Python 3.8
#attmpt at vencrypt
from sys import argv;
import sys;
def makeGrid():
	grid = [];
	size = 256
	for i in range(size):
		row = []
		for j in range(size):
			row.append((i+j) % (size))
		#print(row)
		grid.append(row)
	return grid;

#for reading the keyfile
def read_file(filename):
	with open(filename, "rb") as f:
		data = f.read()
		return data; #currData is binary data of keyfile

if sys.version_info < (3, 6) :
    print("This script requires Python version 3.8 or higher")
    sys.exit(1)


#main method starts here
grid = makeGrid()
try:
	keyfile = argv[1]
	plainfile = argv[3];
	cipherfile = argv[2];
	key = read_file(keyfile)
	#print(key)
except:
	print("please enter in names for keyfile, plaintext and ciphertext");
	exit();
#we instantiate grid here:
#for plaintext and handling the rest of the file aka main 
with open(plainfile, 'wb+') as plain_txt:
	with open(cipherfile, 'rb') as cipher_txt:
		while True:
			data = cipher_txt.read(2048*2048) #data comes from cipherfile
			if not data:
				break;
			#print(data)
			bytedata = bytearray(b'')
			for i in range(len(data)):
				value = data[i] 
				#print(value)
				if not key:
					bytedata.append(data[i])
				else:
					print(key[i % len(key)])
					for x in range(256):
						if(grid[x][key[i % len(key)]] == value):
							bytedata.append(x)
							break;
			#print(bytedata)
			plain_txt.write(bytedata)

cipher_txt.close()
plain_txt.close()
