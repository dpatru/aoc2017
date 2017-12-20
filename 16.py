#! /usr/local/bin/python3

import re
from functools import reduce

# moves = input().split(',')
# print(moves)
line = input()
parse = re.compile(r"(s|x|p)(\w+)/?(\w+)?")
alphabet = "abcdefghijklmnop"
ps = alphabet
ps2 = alphabet # Can we apply partner swaps out of order?
partners=[]
def swapPartners(i,j,arr):
    return arr.translate(str.maketrans(i+j,j+i))
    
for m in re.finditer(parse, line):
    if m:
        g = m.groups()
        if g[0] == "s":
            # print(m.group(0), "spin", g[1])
            x = int(g[1])
            ps = ps[-x:]+ps[:-x]
            ps2 = ps2[-x:]+ps2[:-x]
            
        elif g[0] == "x":
            # print(m.group(0), "exchange", g[1], g[2])
            i, j = int(g[1]), int(g[2])
            if i > j:
                i, j = j, i
            ps = ps[:i]+ps[j]+ps[i+1:j]+ps[i]+ps[j+1:]
            ps2 = ps2[:i]+ps2[j]+ps2[i+1:j]+ps2[i]+ps2[j+1:]
        elif g[0] == "p":
            # print(m.group(0), "partner", g[1], g[2])
            #ps = ps.translate(str.maketrans(g[1]+g[2],g[2]+g[1]))
            ps = swapPartners(g[1],g[2],ps)
            partners.append((g[1],g[2]))
        else:
            print(m, g)
            raise Exception("bad instruction")
        # print(ps)
print(ps)
positionPerm = ps2
namePerm = alphabet
for i,j in partners:
    namePerm = swapPartners(i,j,namePerm)
print("ps2", positionPerm.translate(str.maketrans(alphabet, namePerm)))
# if ps == ps2 then partner swaps can be made out of order.


# part 2 This is tricky because there are two types of permutations
# here: position swaps (spin and exchange) and name swaps (partner
# swaps). These permutations compose differently (See positionPermute
# and namePermute below.) So the compositions are done separately and
# then combined at the end.
#
# To avoid calculating one billion times, we will use the fact that
# applying a permutation n times is still a permutation. So if p^n is
# the permutation which represents applying p n times, then p^2n = p^n
# * 2^n. Notation: let pN represent applying a permutation p 2^N
# times. Then p applied 10 times is the same as p^10 = p^8 * p^2 = p3
# * p1 = p^0b1010.


print()
billion = bin(1000000000)[2:] # one billion in binary.
# billion = bin(10)[2:] 
print('billion', billion)

# Permuting positions involves mapping the permutation to the original
# position.
def positionPermute(x,y): # permute x by y
    return y.translate(str.maketrans(alphabet, x))

# Permuting names involves mapping the original names to the
# permutation. Note that positionPermute != namePermute
def namePermute(x,y):
    return x.translate(str.maketrans(alphabet, y))

# function apply a function to two copies of the argument
def two(f, x): return f(x, x)

# The _Powers arrays holds the powers of two of the permutations. 
positionPowers = [positionPerm]
namePowers = [namePerm]
positions = alphabet
names = alphabet  
for i in range(0,len(billion)): # calculate permutations^2^i 
    if i != 0: # don't compute the first power
        positionPowers.append(two(positionPermute, positionPowers[-1]))
        namePowers.append(two(namePermute, namePowers[-1]))
    if billion[-1-i] == '1':
        positions = positionPermute(positions, positionPowers[i])
        names = namePermute(names, namePowers[i])

print(namePermute(positions, names))

