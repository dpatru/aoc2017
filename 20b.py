#!/usr/local/bin/python3

from collections import namedtuple
import re
from math import sqrt

parse = re.compile(r'p=<(-?\d+),(-?\d+),(-?\d+)>, v=<(-?\d+),(-?\d+),(-?\d+)>, a=<(-?\d+),(-?\d+),(-?\d+)>')

# points are stored as a tuple,
# (manhattan(px,py,pz),px,py,pz,vx,vy,vz,ax,ay,az,i), where the first
# element is the manhattan distance of the position, then the
# position, velocity, and acceleraion, then the id of the point.
Point = namedtuple('Point', 'd x y z vx vy vz ax ay az i t aligned')
points = [] 

def manhattan(x,y,z):
    return abs(x)+abs(y)+abs(z)

def dotproduct (v,w):
    return sum(i*j for i,j in zip(v,w))

# a point is aligned if its position, velocity, and acceleration
# vectors are less than 90deg to each other. This ensures that the
# point will never get closer to the origin.
def isAligned(p,v,a):
    angles = (dotproduct(p,v),
              dotproduct(p,a),
              dotproduct(v,a))
    return all(a >= 0 for a in angles)

def mkPoint(i,x,y,z,vx,vy,vz,ax,ay,az,t=0):
    aligned = isAligned((x,y,z),(vx,vy,vz),(ax,ay,az))
    return Point(manhattan(x,y,z),x,y,z,vx,vy,vz,ax,ay,az,i,t,aligned)

def step(p):
    pos = (p.x+p.vx+p.ax, p.y+p.vy+p.ay, p.z+p.vz+p.az)
    vel = (p.vx+p.ax, p.vy+p.ay, p.vz+p.az)
    acc = (p.ax, p.ay, p.az)
    return Point(manhattan(*pos),
                 *pos, *vel, *acc,
                 p.i, p.t+1,
                 (p.aligned or isAligned(pos,vel,acc)))
                   
def xyz(p):
    return (p.x,p.y,p.z)
def vxyz(p):
    return (p.vx,p.vy,p.vz)
def axyz(p):
    return (p.ax,p.ay,p.az)
    
i=0
while True:
    try:
        points.append(mkPoint(i, *map(int,parse.match(input()).groups())))
        i+=1
        # if i > 10: break # test with small number of points
    except EOFError:
        break

print(i, "points")
# for p in points: print(p)

def removeCollisions(ps): # points (ps) are sorted by distance
    i, j = 0, 0
    collisions = []
    # check for 
    while i < len(ps):
        while j < len(ps) and ps[j].d == ps[i].d:
            j += 1
        sameDistance = [xyz(p) for p in ps[i:j]]
        collisions.extend(x+i for x,p in enumerate(sameDistance)
                          if sameDistance.count(p) > 1)
        i = j
    if collisions:
        # for i in collisions: print("removing", ps[i])
        collisions.reverse() # remove from the end to keep indexes valid
        for x in collisions:
            del ps[x]
    return len(collisions) > 0
        
    
def alwaysFarther(p0, p): # note that manhattan of xyz is ok
                          # because points are sorted.
    return manhattan(*vxyz(p0)) <= manhattan(*vxyz(p)) and \
        manhattan(*axyz(p0)) <= manhattan(*axyz(p))

alone = []
oldlen = len(points)
while len(points) > 0:
    points.sort()
    if removeCollisions(points):
        print("removed collisions")
        pass
    elif all(p.aligned for p in points):
        # everything is aligned, find stragglers
        # print("looking for stragglers")
        while points and \
              all(alwaysFarther(points[0],p) for p in points[1:]):
            # print("found a straggler", points[0])
            alone.append(points.pop(0))
    points = [step(p) for p in points]
    if oldlen != len(points):
        print(len(points),"remaining")
        oldlen = len(points)

print(len(alone), "alone")
            
            
