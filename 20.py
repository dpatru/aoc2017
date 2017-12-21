#!/usr/local/bin/python3

import re
parse = re.compile(r'p=<(-?\d+),(-?\d+),(-?\d+)>, v=<(-?\d+),(-?\d+),(-?\d+)>, a=<(-?\d+),(-?\d+),(-?\d+)>')

def distance(px,py,pz,vx,vy,vz,ax,ay,az):
    big = 2**20
    return (abs(ax)+abs(ay)+abs(az), vx+vy+vz+big*(ax+ay+az))

i=0
distances = []
while True:
    try:
        line = input()
        # print(line)
        m = parse.match(line)
        px,py,pz,vx,vy,vz,ax,ay,az = m.groups()
        distances.append((distance(*map(int, m.groups())), i))
        # print(line,'->',px,py,pz,vx,vy,vz,ax,ay,az)
        i+=1
        # if i > 10:
        #     break
    except EOFError:
        break

print(i, "lines")
print(sorted(distances)[:10], min(distances))
