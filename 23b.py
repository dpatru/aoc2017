#! /usr/local/bin/python3

def isprime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True

h = 0
for i in range(106700, 106700+17000+1, 17):
    if not isprime(i):
        h += 1
print(h)
exit(0)
    
from collections import defaultdict
pc = 0 # program counter
notes = [] # list of notes played
registers = defaultdict(int)
instructions = []

# Arguments can be registers or ints. Make them all ints by mapping
# int arguments to their eponymous register.
def registerArgument(x):
    try:
        i = int(x)
        registers[x] = i
    except ValueError:
        pass
    
# # snd X plays a sound with a frequency equal to the value of X.
# def snd_(x):
#     def f():
#         global notes
#         notes.append(registers[x])
#     return f

# set X Y sets register X to the value of Y.
def set_(x,y):
    def f():
        global registers
        registers[x] = registers[y]
    return f

# add X Y increases register X by the value of Y.
def sub_(x,y):
    def f():
        global registers
        registers[x] -= registers[y]
    return f
mults = 0
# mul X Y sets register X to the result of multiplying the value
# contained in register X by the value of Y.
def mul_(x,y):
    def f():
        global registers
        registers[x] *= registers[y]
        global mults
        mults += 1
    return f

# # mod X Y sets register X to the remainder of dividing the value
# # contained in register X by the value of Y (that is, it sets X to the
# # result of X modulo Y).
# def mod_(x,y):
#     def f():
#         global registers
#         registers[x] %= registers[y]
#     return f

# # rcv X recovers the frequency of the last sound played, but only when
# # the value of X is not zero. (If it is zero, the command does
# # nothing.)
# def rcv_(x):
#     def f():
#         global registers
#         global notes
#         if registers[x] != 0:
#             print("last sound was", notes[-1])
#             raise Exception # program ends
#     return f
        
# jgz X Y jumps with an offset of the value of Y, but only if the
# value of X is not zero. (An offset of 2 skips the next instruction,
# an offset of -1 jumps to the previous instruction, and so on.)
def jnz_(x,y):
    def f():
        global registers
        global pc
        if registers[x] != 0:
            pc += registers[y]-1
    return f
        
compileInstruction = dict(
    set= set_,
    sub= sub_,
    mul= mul_,
    jnz= jnz_ )

import fileinput
for line in fileinput.input():
    instr, *args = line.split()
    for a in args: registerArgument(a)
    instructions.append(compileInstruction[instr](*args))

registers['a'] = 1

oldh = registers['h']

while True:
    try:
        instructions[pc]()
        pc += 1
        if oldh != registers['h']:
            print('h changed from',oldh,'to',registers['h'])
            oldh = registers['h']
    except IndexError:
        break
        
print("mults",mults)
print("registers[h]",registers[h])
