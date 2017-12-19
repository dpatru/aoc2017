#! /usr/local/bin/python3

def ga(x):
    while True:
        x = (x * 16807) % 2147483647
        # return x # part 1
        if x % 4 == 0:
            return x

def gb(x):
    while True:
        x = (x * 48271) % 2147483647
        # return x # part 1
        if x % 8 == 0:
            return x

def matches(x,y):
    return (x & 0xffff) == (y & 0xffff)

A = 634
B = 301
#A = 65 # test
#B = 8921 # test

c = 0
for i in range(5000000):
#for i in range(5):
    A,B = ga(A),gb(B)
    # print(A, B)
    if matches(A,B):
        c += 1

print(c, "matches")
