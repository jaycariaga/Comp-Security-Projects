#!/usr/bin/python3
from sys import argv;
import sys;
#Jason Cariaga
#171001720
#done using Python 3.8

import hashlib

m = hashlib.sha256()
m.update(b" goteeem")
print(m.digest())