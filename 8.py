#! /usr/local/bin/python3

# run as: ./7.py < 7.input.txt
from collections import defaultdict
import re

register = defaultdict(int)

def doTest(r, tst, v):
    if tst == '==':
        return True if register[r] == v else False
    elif tst == '<':
        return True if register[r] < v else False
    elif tst == '<=':
        return True if register[r] <= v else False
    elif tst == '>':
        return True if register[r] > v else False
    elif tst == '>=':
        return True if register[r] >= v else False
    elif tst == '!=':
        return True if register[r] != v else False
    else:
        raise Exception("bad test operator")

def doAction(r, op, amt):
    if op == 'inc':
        register[r] += amt
    elif op == 'dec':
        register[r] -= amt
    else:
        raise Exception("bad action operator")

best = 0

while True:
    # https://stackoverflow.com/a/42891677/268040
    try:
        line = input()
    except EOFError:
        break
    if not line:
        break
    reg, op, amt, reg2, tst, val = re.split('\s+if\s+|\s+', line)
    if doTest(reg2, tst, int(val)):
        doAction(reg, op, int(amt))
        b = max(register.values())
        if b > best:
            best = b

        


print(max(register.values()))
print(best)
