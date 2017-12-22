#!/usr/local/bin/python3

import re
from math import sqrt

def lastGroup(n):
    x = 3
    g = 0
    r = 0
    while x < n:
        if x % 2 == 0:
            g = 2
            r = 3
        else:
            g = 3
            r = 4
        x /= g
        x *= r
    return g

def chooseGroup(sq,after=None):
    return lastGroup(int(sqrt(len(sq)))) if after else \
        2 if len(sq) % 4 == 0 else 3

def showgrouped(sq, g=None):
    if g is None: return showgrouped(sq,chooseGroup(sq))
    l = int(sqrt(len(sq)))
    print("showgrouped", g, sq)
    vsep = '\n'+'+'.join('-'*g for i in range(0,l,g))+'\n'
    # print('g', g, 'sep',vsep)
    
    s = vsep.join('\n'.join('|'.join(sq[j*l+k:j*l+k+g]
                                     for k in range(0,l,g))
                            for j in range(i,i+g))
                  for i in range(0,l,g))
    print(s)
    print()

def showflat(sq):
    print("showflat", sq)
    l = int(sqrt(len(sq)))
    for i in range(l):
        print(sq[i*l: i*l+l])
    print()

def group(sq, g=None):
    if g is None: return group(sq, chooseGroup(sq))
    l = int(sqrt(len(sq)))
    return ['/'.join(sq[k*l+i:k*l+i+g] for k in range(j,j+g))
            for j in range(0,l,g)
            for i in range(0,l,g)]



def flatten(sq):
    l = int(sqrt(len(sq)))
    return ''.join(''.join(''.join(x)
                           for x in zip(*[s.split('/')
                                          for s in sq[i*l:i*l+l]]))
                   for i in range(l))


def rotate180(sq):
    return sq[::-1]
def transpose(sq):
    l = int(sqrt(len(sq)))
    return ''.join(sq[i::l] for i in range(l))
def fliph(sq):
    l = int(sqrt(len(sq)))
    return ''.join(sq[i*l:i*l+l][::-1] for i in range(l))
def flipv(sq):
    return fliph(rotate180(sq))
def rotateLeft(sq):
    return flipv(transpose(sq))
def rotateRight(sq):
    return transpose(flipv(sq))
def rotate0(sq): return sq
def variations(sq):
    return set(f(r(sq))
               for r in (rotate0,rotateLeft,rotateRight,rotate180)
               for f in (rotate0,fliph,flipv))

def testTransforms():
    # sq = ('#..#........#..#')
    # sq = ('##..........#..#')
    sq = 'abcdefghijklmnop'
    
    showflat(sq)
    showgrouped(sq,2)
    print('group2', group(sq,2))
    print('flatten', flatten(group(sq,2)))
    print('rotate180', rotate180(sq))
    showflat(rotate180(sq))
    print('transpose', transpose(sq))
    showflat(transpose(sq))
    print('fliph', fliph(sq))
    showflat(fliph(sq))
    print('flipv', flipv(sq))
    showflat(flipv(sq))
    print('rotateLeft', rotateLeft(sq))
    showflat(rotateLeft(sq))
    print('rotateRight', rotateRight(sq))
    showflat(rotateRight(sq))
    
    print('variations')
    for s in variations(sq):
        showflat(s)


import fileinput

trans = dict()

for line in fileinput.input():
    i, o = line.strip().split(' => ')
    # print('i',i,'o',o)
    for j in variations(i.replace('/','')):
        trans[j] = o

for k,v in trans.items():
    print(k, v)
    
s = '.#...####'
# for x in variations(g):
#     if x in trans:
#         print(x,"in trans")
#     else:
#         print(x, 'not in trans')

for i in range(18):
    print('-'*30)
    print(s.count('#'),'pixels on at',i)
    g = chooseGroup(s)
    # showgrouped(s,g)
    s = group(s,g)
    # print(g)
    s = flatten([trans[x.replace('/','')] for x in s])
    # showgrouped(s, 3 if g == 2 else 4)
else: print(s.count('#'),'pixels on at',i+1)
    
    
    
    
# 3
# 4=2*2
# 2*3=6=3*2
# 3*3=9
# 3*4=12=6*2
# 6*3=18

# 3 * 4/3 * 3/2 * 3/2
# 3   4     6     9

# 2^0 3 2^2  2*3
