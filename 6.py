#! /usr/local/bin/python3

import numpy as np

xs = []

def rearrange(bs):
    seen = set()
    c = 0
    while tuple(bs) not in seen:
        seen.add(tuple(bs))
        i = np.argmax(bs)
        blocks = bs[i]
        bs[i] = 0
        while blocks > 0:
            i = (i + 1) % len(bs)
            bs[i] += 1
            blocks -= 1
        c += 1
    return c


while True:
    # https://stackoverflow.com/a/42891677/268040
    try:
        line = input()
    except EOFError:
        print("EOL error")
        break
    if not line:
        print("error")
    banks = [int(x) for x in line.split()]
    print("banks = ", banks)
    print("count = ", rearrange(banks))
    break





