#! /usr/bin/env python3

from collections import defaultdict,namedtuple
from functools import reduce
import re

parse = re.compile(r'(\d+)/(\d+)')
import fileinput
parts = [tuple(map(int,parse.match(line).groups()))
         for line in fileinput.input()]
# print(len(parts), parts)
partlookup = defaultdict(list) # port -> part index, 2 entries per part
# for i,(j,k) in enumerate(parts):
#     partlookup[j].append(i)
#     partlookup[k].append(i)
for i,p in enumerate(parts):
    for x in p:
        partlookup[x].append(i)

unfinished = [((i,),max(parts[i])) for i in partlookup[0]]
bestval = 0
bestseq = ()
while unfinished:
    seq, i = unfinished.pop()
    final = True
    for j in partlookup[i]:
        if j not in seq:
            final = False
            x,y = parts[j]
            unfinished.append((seq + (j,), x if y == i else y))
    if final:
        val = sum(x for x in parts[i] for i in seq)
        if bestval < val:
            bestval = val
            bestseq = seq
        print('best', bestval, bestseq)

exit(0)
        
# for i in sorted(partlookup.keys()):
#     print(i, partlookup[i])
# for i,p in partlookup.items():
#     print(i, p)

Chain = namedtuple('Chain', 'val seq port')
def inc(chain, i):
    x,y = parts[i]
    return Chain(chain.val+x+y, chain.seq+(i,), x if chain.port == y else y)
def mkChain(seq):
    return reduce(inc, seq, Chain(0,(),0))

# When all you have is a hammer, you try to see every problem as a
# nail. Dikstra's shortest path argument allows cutoffs and pruning. Can we use this idea here?

# Alternatively, what can we tell about the solution chains just by
# looking? Ports link to other like ports in pairs. Where there are
# odd number of ports, either we have to end in that port, or the
# component doesn't get used.

# for p  in sorted(partlookup.keys()):
#     indexes = partlookup[p]
#     if len(indexes) %2 == 1:
#         print(p, len(indexes))

def build():
    unfinished=[mkChain([i]) for i in partlookup[0]]
    best = Chain(0,(),0)
    while unfinished:
        c = unfinished.pop()
        while True: # build a full chain, putting the partial chains on the unfinished stack
            nextParts = [p for p in partlookup[c.port] if p not in c.seq]
            if not nextParts: # finished a sequence
                if c.val > best.val:
                    best = c
                    print(len(unfinished), 'unfinished, best',best)
                break
            else:
                n = nextParts.pop()
                c = inc(c,n)
                unfinished.extend(inc(c,p) for p in nextParts)

build()
