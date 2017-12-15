#! /usr/local/bin/python3

# run as: ./7.py < 7.input.txt
from collections import defaultdict
import re
from operator import xor
from functools import reduce

def reverse(l, i, s):
    # print("reversing", i, s, l)
    while s > 0:
        j = (i+s-1)%len(l)
        l[i], l[j] = l[j], l[i]
        s -= 2
        i = (i + 1)%len(l)
    # print("->", l)
    # print()

def knot(line):
    sizes = list(map(ord, line)) + [17,31,73,47,23]
    lst = list(range(256))
    skip = 0
    pos = 0
    for _ in range(64):
        for s in sizes:
            reverse(lst, pos, s)
            pos = (pos + s + skip)%256
            skip += 1
            # print("list is", lst)
    print("sparse hash", lst)
    h = ''.join(hex(reduce(xor, lst[16*i:16*i+16]))[2:].zfill(2)
                for i in range(16))
    print("dense hash", h)
              
while True:
    # https://stackoverflow.com/a/42891677/268040
    try:
        line = input()
    except EOFError:
        break
    if not line:
        print("No line")
        next
    knot(line)
