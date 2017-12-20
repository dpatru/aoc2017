#! /usr/local/bin/python3

import re
from functools import reduce

steps = 329 # input
buf = [0]
pos = 0
#for i in range(1, 2017+1):
for i in range(1, 50000000+1):
    pos = ((pos + steps) % len(buf)) + 1
    buf.insert(pos, i)
    if i % 100000 == 0: print(i)
#print(buf[(pos+1)%len(buf)])
i = buf.index(0)
print(buf[(i+1)%len(buf)])
