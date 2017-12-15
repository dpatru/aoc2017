#! /usr/local/bin/python3

# run as: ./7.py < 7.input.txt
from collections import defaultdict
import re

def reverse(l, i, s):
    print("reversing", i, s, l)
    while s > 0:
        l[i], l[(i+s-1)%len(l)] = l[(i+s-1)%len(l)], l[i]
        s -= 2
        i = (i + 1)%len(l)
    print("->", l)
    print()
    
while True:
    # https://stackoverflow.com/a/42891677/268040
    try:
        line = input()
    except EOFError:
        break
    if not line:
        print("No line")
        next
    sizes = map(int, re.split(',\s*', line))
    lst = list(range(256))
    # lst = list(range(5)) # practice
    skip = 0
    pos = 0
    for s in sizes:
        reverse(lst, pos, s)
        pos = (pos + s + skip)%len(lst)
        skip += 1
        print("list is", lst)
    print("product of first two is", lst[0] * lst[1])
    print()
