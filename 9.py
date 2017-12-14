#! /usr/local/bin/python3

# run as: ./7.py < 7.input.txt
from collections import defaultdict
import re

level = 0
score = 0
groups = 0
garbage = 0

while True:
    # https://stackoverflow.com/a/42891677/268040
    try:
        line = input()
    except EOFError:
        break
    if not line:
        print("No line")
        next
    print("Line:", line)
    line = list(line)
    while len(line) > 0:
        c = line.pop(0)
        if c == "{":
            level += 1
            score += level
        elif c == "<": # garbage, stay here until you get out
            while True:
                c = line.pop(0)
                if c == ">":
                    break
                elif c == "!":
                    line.pop(0)
                else:
                    garbage += 1
                    pass
        elif c == "}":
            level -= 1
            groups += 1
        else:
            pass
            
        if level < 0:
            raise Exception("extra }")
    print("Groups =", groups)
    print("Score =", score)
    print("Garbage =", garbage)
    print("Level =", level)
    print()
    level = score = groups = garbage = 0
