#!/usr/bin/python3

import sys

filename = sys.argv[1]

with open(filename, 'rb') as f:
    byte_data = f.read()

with open(filename, 'w') as w:
    w.write(byte_data.decode('UTF-8', errors='ignore'))
