#! /usr/local/bin/python3

# run as: ./11.py < 11.input.txt

from functools import reduce

def normalize(x,y,z):
    x += y; z += y; y = 0
    if (x>0) == (z>0): # same sign
        m = min(x, z, key=abs)
        x -= m; z -= m; y = m
    return (x,y,z)


def steps(coords):
    return sum(map(abs, normalize(*coords)))

longest = 0

def reduceMove(coords, move):
    x, y, z = coords
    c = (x,y+1,z) if move == 'n' else \
        (x,y-1,z) if move == 's' else \
        (x+1,y,z) if move == 'ne' else \
        (x-1,y,z) if move == 'sw' else \
        (x,y,z+1) if move == 'nw' else \
        (x,y,z-1) if move == 'se' else \
        move / 0  # raise Exception("bad move: "+move)
    global longest
    longest = max(longest, steps(c))
    return c

def reduceMoves(moves):
    return reduce(reduceMove, moves, (0,0,0))


while True:
    # https://stackoverflow.com/a/42891677/268040
    try:
        line = input()
    except EOFError:
        break
    if not line:
        print("No line")
        next
    coords = normalize(*reduceMoves(line.split(',')))
    print("coords =", coords)
    print("move =", steps(coords))
    print("longest =", longest)
