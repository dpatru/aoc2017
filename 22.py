#!/usr/local/bin/python3

from collections import defaultdict
import re
import fileinput

infected = defaultdict(bool) # defaults to false

yoffset = xoffset = None
y = 0
for line in fileinput.input():
    if xoffset is None:
        print(len(line.strip()), line)
        yoffset = int(len(line.strip())/2)
        xoffset = -yoffset
    for m in re.finditer('#',line):
        infected[(m.start()+xoffset, y+yoffset)] = True
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
for t in range(10000):
    # print('t', t, 'pos', pos, 'vel', vel, 'infected', infected[pos])
    if infected[pos]:
        vel = turnr(vel)
        # print('turning right, vel =', vel)
        infected[pos] = False
    else:
        vel = turnl(vel)
        # print('turning left, vel =', vel)
        infected[pos] = True
        caused += 1
    pos = move(pos,vel)

print(caused)
