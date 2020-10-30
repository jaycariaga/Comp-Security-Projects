#Jason Cariaga
#second attmpt at vencrypt using different approach
from sys import argv;
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

#main method starts here
grid = makeGrid()
try:
	keyfile = argv[1]
	plainfile = argv[2];
	cipherfile = argv[3];
	key = read_file(keyfile)
	#print(key)
except:
	print("please enter in names for keyfile, plaintext and ciphertext");
	exit();
#we instantiate grid here:
#for plaintext and handling the rest of the file aka main 
with open(plainfile, 'rb') as plain_txt:
	with open(cipherfile, 'wb+') as cipher_txt:
		while True:
			data = plain_txt.read(2048*2048) #comes from plaintext file
			if not data:
				break;
			#print(data) prints out b'...'
			#print(key) prints out b'...'
			bytedata = bytearray(b'')
			print(data)
			for i in range(len(data)):
				rowbyte = data[i] #row represents the read plaintext, columns are the key reps
				if not key:
					bytedata.append(data[i])
				else:
					colbyte = key[i % len(key)]
					print(colbyte)
					bytedata.append(grid[rowbyte][colbyte])
			print(bytedata)
			cipher_txt.write(bytedata)

cipher_txt.close()
plain_txt.close()

