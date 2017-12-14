#! /usr/local/bin/python3

# Memory is arranged in a spiral. The spiral forms squares, with the
# lower right cell having the address as the square of an odd number.
# The sequence looks like: 1, 9, 25, 49, ...
#
# Given an address, we can count up by the squares of successsive odd
# numbers until we've found the square containing the address.  From
# there, we need to find out how many steps to reach the origin.
#
# (2n+1)^2 gives the address of the bottom-right cell.
#
# How many cells in the outer layer?
# (2n+1)^2 - (2n - 1)^2 = 4n^2 + 4n + 1 - (4n^2 - 4n + 1) = 8n
# 2(2n + 1)*2 = 8n + 4 is the derrivative. It should correspond to the
# number of cells in the outer layer.


from math import sqrt, ceil
def level(cell):
    return ceil((ceil(sqrt(cell))-1)*.5)

def offset(cell):
    l = level(cell)
    return abs(((l*2+1)**2 - cell) % (2*l) - l)

def steps(cell):
    return level(cell) + offset(cell)

print("steps = ", steps(368078))

print("Part 2")

# A cell never has to sum more than four previous cells: the cells to
# its interior (maximum three) and its previous cell in its own ring.

coords = [(0,0)]
sums = {(0,0):1}
x = 1
y = 0
def calculate(x,y):
    coords.append((x,y))
    sums[(x,y)] = 0
    for i in (-1,0,1):
        for j in (-1,0,1):
            if i == 0 and j == 0:
                pass
            elif (x+i,y+j) not in sums:
                pass
            else:
                sums[(x,y)] += sums[(x+i,y+j)]
    print("calculating ", x, y, sums[(x,y)])

for sq in range(1, 5):
    side = list(range(2*sq))
    print("side =", side)
    for rightSide in side:
        calculate(x,y)
        y += 1
    x -= 1; y -= 1
    for topSide in side:
        calculate(x,y)
        x -= 1
    x += 1; y -= 1
    for leftSide in side:
        calculate(x,y)
        y -= 1
    x += 1; y += 1
    for bottomSide in side:
        calculate(x,y)
        x += 1

for i, c in enumerate(coords):
    print(i, sums[c])
    if sums[c] > 368078:
        break
