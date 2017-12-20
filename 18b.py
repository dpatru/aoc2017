#! /usr/local/bin/python3

from collections import defaultdict, deque

class Machine:
    def __init__(self, machineName):
        self.registers = defaultdict(int)
        self.machineName = self.registers['p'] = machineName
        self.pc = 0 # program counter
        self.instructions = []
        self.inputQ = deque()
        self.waiting = False
        self.sent = 0

    def setNeighbor(self, n):
        self.neighbor = n

    def dump(self):
        print("dumping machine", self.machineName)
        for i in range(len(self.instructions)):
            print("instructions[",i,"] =", self.instructions[i])
        print("pc", self.pc)
        for i in self.registers:
            print("registers[",i,"] =", self.registers[i])
        print("inputQ =", self.inputQ)
        print()
        
    # Arguments can be registers or ints. Make them all ints by mapping
    # int arguments to their eponymous register.
    def registerArgument(self, x):
        try:
            i = int(x)
            self.registers[x] = i
        except ValueError:
            pass
        
    # snd X sends the value of X to the other program. These values
    # wait in a queue until that program is ready to receive
    # them. Each program has its own message queue, so a program can
    # never receive a message it sent.
    def snd_(self, x):
        def snd__():
            self.neighbor.inputQ.append(self.registers[x])
            self.neighbor.waiting = False
            self.sent += 1
            return True # yield
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

    # rcv X receives the next value and stores it in register X. If no
    # values are in the queue, the program waits for a value to be
    # sent to it. Programs do not continue to the next instruction
    # until they have received a value. Values are received in the
    # order they are sent.
    def rcv_(self,x):
        def rcv__():
            if len(self.inputQ) == 0:
                self.waiting = True
                return True
            else:
                self.registers[x] = self.inputQ.popleft();
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
        # print("adding instructon", instr, args)
        for arg in args: self.registerArgument(arg)
        self.instructions.append(self.compileInstruction[instr](self, *args))

    def run(self):
        if self.waiting: return
        try:
            while True:
                # print("Machine", self.machineName, "running instructions[", self.pc, "] = ", self.instructions[self.pc])
                r = self.instructions[self.pc]()
                if r and self.waiting:
                    return # don't incr pc, restart at this instruction.
                self.pc += 1
                if r: return # yield
        except:
            print("Run error:")
            self.dump()

# Top level
mach0 = Machine(0)
mach1 = Machine(1)
mach1.neighbor, mach0.neighbor = mach0, mach1

while True:
    try:
        instr, *args = input().split()
        mach0.addInstruction(instr, *args)
        mach1.addInstruction(instr, *args)
    except EOFError:
        break

def dump():
    print("Dumpingeadlocked!")
    mach0.dump()
    mach1.dump()
    # raise Exception("Deadlocked")

c = 0
while True:
    if not mach0.waiting:
        if c % 1000 == 0:
            pass # print(c, "mach0.sent", mach0.sent)
        mach0.run()
    if not mach1.waiting:
        if c % 1000 == 0:
            pass # print(c, "mach1.sent", mach1.sent)
        mach1.run()
    if mach0.waiting and mach1.waiting:
        print("Deadlocked after", c, "cycles!")
        # dump()
        print("mach1.sent", mach1.sent)
        break
    c += 1
    if c > 10000:
        print("stopping after 10000")
        dump
        break
        
print("end")
