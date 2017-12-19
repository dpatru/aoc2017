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
    # print("sparse hash", lst)
    h = ''.join(hex(reduce(xor, lst[16*i:16*i+16]))[2:].zfill(2)
                for i in range(16))
    # print("dense hash", h)
    return h

h2b = {
    '0':'0000', '1':'0001', '2':'0010', '3':'0011',
    '4':'0100', '5':'0101', '6':'0110', '7':'0111',
    '8':'1000', '9':'1001', 'A':'1010', 'B':'1011',
    'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111',
    'a':'1010', 'b':'1011',
    'c':'1100', 'd':'1101', 'e':'1110', 'f':'1111'}

def hex2bin(h):
    return ''.join(h2b[x] for x in h)
    
key = "hwlqcszp"

# part 1
used = 0
for i in range(128):
    k = key+'-'+str(i)
    x = hex2bin(knot(k))
    used += x.count('1')
    # print(x, k, x.count('1'))
print("used", used)

# part 2: Part 2 asks for the number of groups of cells. Save the grid
# in a dict and then traverse it looking for groups.
def bin2bool(xs):
    return [x == '1' for x in xs]

grid=[]
for i in range(128):
    k = key+'-'+str(i)
    grid.append(bin2bool(hex2bin(knot(k))))

seen = dict()
next_group = 0

X = 128
Y = 128
def explore(i,j):
    stack = [(i,j)]
    while len(stack) > 0:
        i,j = stack.pop(0)
        # print("exploring", i, j, "for group", next_group)
        if (i,j) not in seen and 0 <= i < X and 0 <= j < Y and grid[i][j]:
            seen[(i,j)]=True
            stack.extend((i+x,j) for x in [-1,0,1])
            stack.extend((i,j+x) for x in [-1,0,1])


# for i in range(X):
#     print(["1" if grid[i][j] else "0" for j in range(Y)])

for i in range(X):
    for j in range(Y):
        if (i,j) not in seen:
            if grid[i][j]:
                explore(i,j)
                next_group += 1
print(next_group, "groups")

