#!/usr/local/bin/python3

from collections import defaultdict
import re
import fileinput

infected = defaultdict(int) # defaults to 0
# 0 - clean
# 1 - weakened
# 2 - infected
# 3 - flagged
#
# To move the node to the next state, add 1 mod 4.

yoffset = xoffset = None
y = 0
for line in fileinput.input():
    if xoffset is None:
        print(len(line.strip()), line)
        yoffset = int(len(line.strip())/2)
        xoffset = -yoffset
    for m in re.finditer('#',line):
        infected[(m.start()+xoffset, y+yoffset)] = 2
    y -= 1

for k,v in infected.items():
    print(k, v)
    
pos = (0,0)
vel = (0,1)
def turnl(v):
    x,y=v
    return (-y,x)
def turnr(v):
    x,y=v
    return (y,-x)
def move(p,v):
    return (p[0]+v[0],p[1]+v[1])

# verify direction changes
# for p in [(0,1),(1,0),(0,-1),(-1,0)]:
#     print(p, turnl(turnl(turnl(p))), turnr(p))

caused = 0
for t in range(10000000):
    # print('t', t, 'pos', pos, 'vel', vel, 'infected', infected[pos])
    i = infected[pos]
    vel = turnl(vel) if i==0 else \
          vel if i==1 else \
          turnr(vel) if i==2 else \
          turnr(turnr(vel)) if i==3 else \
          1/0 # raise error vel is not known
    infected[pos] = (i + 1) % 4
    if infected[pos] == 2: 
        caused += 1
    pos = move(pos,vel)

print(caused)
