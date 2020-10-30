from sys import argv;
#Jason Cariaga
#171001720



x = [0, 1, 2, 3]
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