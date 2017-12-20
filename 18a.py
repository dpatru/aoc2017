#! /usr/local/bin/python3

from collections import defaultdict

class Machine:
    def __init__(self):
        self.pc = 0 # program counter
        self.notes = [] # list of notes played
        self.registers = defaultdict(int)
        self.instructions = []

    def dump(self):
        print("dump:")
        for i in range(len(self.instructions)):
            print("instructions[",i,"] =", self.instructions[i])
        print("pc", self.pc)
        for i in range(len(self.registers)):
            print("registers[",i,"] =", self.registers[i])
        print("notes =", self.notes)
        
    # Arguments can be registers or ints. Make them all ints by mapping
    # int arguments to their eponymous register.
    def registerArgument(self, x):
        try:
            i = int(x)
            self.registers[x] = i
        except ValueError:
            pass
        
    # snd X plays a sound with a frequency equal to the value of X.
    def snd_(self, x):
        def snd__():
            self.notes.append(self.registers[x])
        return snd__
        
    # set X Y sets register X to the value of Y.
    def set_(self,x,y):
        def set__():
            self.registers[x] = self.registers[y]
        return set__

    # add X Y increases register X by the value of Y.
    def add_(self,x,y):
        def add__():
            self.registers[x] += self.registers[y]
        return add__

    # mul X Y sets register X to the result of multiplying the value
    # contained in register X by the value of Y.
    def mul_(self,x,y):
        def mul__():
            self.registers[x] *= self.registers[y]
        return mul__

    # mod X Y sets register X to the remainder of dividing the value
    # contained in register X by the value of Y (that is, it sets X to
    # the result of X modulo Y).
    def mod_(self,x,y):
        def mod__():
            self.registers[x] %= self.registers[y]
        return mod__

    # rcv X recovers the frequency of the last sound played, but only
    # when the value of X is not zero. (If it is zero, the command
    # does nothing.)
    def rcv_(self,x):
        def rcv__():
            if self.registers[x] != 0:
                print("last sound was", self.notes[-1])
                raise Exception # program ends
        return rcv__
        
    # jgz X Y jumps with an offset of the value of Y, but only if the
    # value of X is greater than zero. (An offset of 2 skips the next
    # instruction, an offset of -1 jumps to the previous instruction,
    # and so on.)
    def jgz_(self,x,y):
        def jgz__():
            if self.registers[x] > 0:
                self.pc += self.registers[y]-1
        return jgz__
        
    compileInstruction = dict(
        snd= snd_,
        set= set_,
        add= add_,
        mul= mul_,
        mod= mod_,
        rcv= rcv_,
        jgz= jgz_ )

    def addInstruction(self, instr, *args):
        print("adding instructon", instr, args)
        for arg in args: self.registerArgument(arg)
        self.instructions.append(self.compileInstruction[instr](self, *args))

    def run(self):
        try:
            while True:
                print("running instructions[", self.pc, "] = ",
                      self.instructions[self.pc])
                self.instructions[self.pc]()
                self.pc += 1
        except:
            print("Run error:")
            self.dump()
            
mach = Machine()

while True:
    try:
        instr, *args = input().split()
        mach.addInstruction(instr, *args)
    except EOFError:
        break

mach.run()
        
