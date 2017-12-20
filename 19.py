#! /usr/local/bin/python3

maze=dict()
y = 0
X = 0
while True:
    try:
        for x, c in enumerate(input()):
            if x >= X: X = x+1
            if y == 0 and c == '|':
                pos = (x,y)
            maze[(x,y)] = c
        y += 1
    except:
        break
Y = y
print('max coordinate (X,Y)', X, Y)
print('start =', pos)
direction = (0, 1)
directions = [(0,1),(1,0),(0,-1),(-1,0)]
paths = ['|','-','|','-']
def move(p, d):
    x,y = p
    dx,dy = d
    return (x+dx,y+dy)
def reverse(d):
    x,y = d
    return (-1*x, -1*y)
def inbounds(p):
    x,y = p
    return 0<=x<X and 0<=y<Y

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters = []
steps = 0
while True:
    try:
        print(pos, maze[pos], direction)
        if not inbounds(pos):
            print("out of bounds")
            raise Exception("out of bounds")
        
        if maze[pos] == '+': # change direction
            for d,p in zip(directions, paths):
                if d != reverse(direction):
                    pos2 = move(pos, d)
                    if inbounds(pos2):
                        if maze[pos2] == p:
                            direction = d
                            print("moving towards", direction)
                            break
                        elif maze[pos2] in alphabet:
                            direction = d
                            letters.append(maze[pos2])
                            print("picked up letter:", letters)
                            print("moving towards", direction)
                            break
        elif maze[pos] in alphabet:
            letters.append(maze[pos])
            print("picked up letter:", letters)
        elif maze[pos] == ' ':
            print("Reached the end")
            raise Exception("Reached the end")
        pos = move(pos, direction)
        steps += 1
    except:
        print("letters:", ''.join(letters))
        print("steps:", steps)
        break
    
    
