#! /usr/local/bin/python3

# run as: ./13.py < 13.input.txt
from collections import defaultdict
import re


fdepth = []
frange = []

while True:
    # https://stackoverflow.com/a/42891677/268040
    try:
        line = input()
    except EOFError:
        break
    if not line:
        break
    d, r = map(int, line.split(': '))
    fdepth.append(d)
    frange.append(r)
    # print("line", line)
    # print("depth", d, fdepth[-1])
    # print("range", r, frange[-1])

# Part 1
# penalty = 0
# for i in range(len(fdepth)):
#     d, r = fdepth[i], frange[i]
#     print(d, r, d % (2*r-2), r*d)
#     if d % (2*r-2) == 0 :
#         penalty += d*r
# print(penalty)

# Part 2
for delay in range(10000000):
    # print("delay", delay)
    for i in range(len(fdepth)):
        d, r = fdepth[i], frange[i]
        # print(d + delay, (delay+d) % (2*r-2), r*d)
        if (d + delay) % (2*r-2) == 0 :
            break
    else:
        print(delay)
        break
else:
    print("no delay found")
    
