#! /usr/bin/env python3

import re
import fileinput
from collections import namedtuple, defaultdict

State = namedtuple('State','write0 move0 cont0 write1 move1 cont1')

trans = dict(
    A=State(write0=1,move0=1,cont0='B',
            write1=0,move1=-1,cont1='B'),
    B=State(write0=1,move0=-1,cont0='C',
            write1=0,move1=1,cont1='E'),
    C=State(write0=1,move0=1,cont0='E',
            write1=0,move1=-1,cont1='D'),
    D=State(write0=1,move0=-1,cont0='A',
            write1=1,move1=-1,cont1='A'),
    E=State(write0=0,move0=1,cont0='A',
            write1=0,move1=1,cont1='F'),
    F=State(write0=1,move0=1,cont0='E',
            write1=1,move1=1,cont1='A'))

tape = defaultdict(bool)

position, state  = 0, 'A'
maxSteps = 12861455
for step in range(maxSteps):
    t = trans[state]
    if tape[position]:
        tape[position] = t.write1
        position += t.move1
        state = t.cont1
    else:
        tape[position] = t.write0
        position += t.move0
        state = t.cont0

print(sum(tape.values()))
