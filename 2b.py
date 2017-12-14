#! /usr/local/bin/python3

from itertools import tee

def quotient(it1, it2):
    for i in it1:
        it2, it3 = tee(it2) 
        for j in it3:
            if i > j and i / j == int(i / j):
                print(i, j, " work")
                print(" ")
                return int(i / j)
            # else:
            #     print(i, j, "don't work")
    raise Exception("no Quotient")
    
s = 0
done = False
while True:
    try:
        line = input()
    except EOFError:
        done = True
    if not line or done:
        print("sum is ", s)
        break
    # print("line is: ", line)
    l1, l2 = tee(map(int, line.split()))
    s += quotient(l1, l2)

    # print("max is ", ma, ", min is ", mi, ", s is ", s)



