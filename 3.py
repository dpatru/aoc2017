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

print(steps(368078))
