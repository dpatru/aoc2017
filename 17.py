#! /usr/local/bin/python3

from collections import deque

steps = 329 # input
buf = deque([0]) # will always insert at the beginning
for i in range(1, 2017+1):
    buf.rotate(-1*(steps + 1) % len(buf))
    buf.appendleft(i)

print(buf[1])

# part 2
steps = 329 # input
buf = deque([0]) # will always insert at the beginning
for i in range(1, 50000000+1):
    buf.rotate(-1*(steps + 1) % len(buf))
    buf.appendleft(i)
    if i % 200000 == 0: print("i", i) # see progress
i = (buf.index(0) + 1)%len(buf)
print(buf[i])
