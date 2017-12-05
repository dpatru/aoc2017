#! /usr/local/bin/python3

from itertools import tee

s = 0
while True:
    line = input()
    if not line:
        print("sum is ", s)
        break
    # print("line is: ", line)
    l1, l2 = tee(map(int, line.split()))
    mi = min(l1);    ma = max(l2); 
    s += ma - mi
    # print("max is ", ma, ", min is ", mi, ", s is ", s)



