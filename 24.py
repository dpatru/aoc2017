#! /usr/bin/env python3

from collections import defaultdict,namedtuple
from functools import reduce
import re

parse = re.compile(r'(\d+)/(\d+)')
import fileinput
parts = tuple(tuple(map(int,parse.match(line).groups()))
              for line in fileinput.input())
# print(len(parts), parts)
partlookup = defaultdict(list) # port -> part index, 2 entries per part
for i,p in enumerate(parts):
    for x in p:
        partlookup[x].append(i)

# print('parts')
# for i,p in enumerate(parts):
#     print(i,p)
# print()


def orderSeq(seq):
    prev = 0
    r = []
    for p in [parts[i] for i in seq]:
        if p[0] == prev:
            r.append(p)
            prev = p[1]
        else:
            r.append(p[::-1])
            prev = p[0]
    return r

unfinished = [((i,),max(parts[i])) for i in partlookup[0]]
bestval = 0
bestseq = ()

sequences = 0
while unfinished:
    seq, i = unfinished.pop()
    final = True
    for j in partlookup[i]:
        if j not in seq:
            final = False
            x,y = parts[j]
            unfinished.append((seq + (j,), x if y == i else y))
    if final:
        sequences += 1
        val = sum(sum(parts[i]) for i in seq)
        if bestval < val:
            bestval = val
            bestseq = seq
            print(len(unfinished),'unfinished, best', bestval, bestseq, orderSeq(bestseq))

print(sequences,'sequences tried')


# exit(0)
        
# for i in sorted(partlookup.keys()):
#     print(i, partlookup[i])
# for i,p in partlookup.items():
#     print(i, p)

Chain = namedtuple('Chain', 'val seq port')
def inc(chain, i):
    x,y = parts[i]
    return Chain(val=chain.val+x+y,
                 seq=chain.seq+(i,),
                 port = x if chain.port == y else y)
def mkChain(seq):
    return reduce(inc, seq, Chain(val=0,seq=(),port=0))


sequences = 0
def build():
    unfinished=[mkChain([i]) for i in partlookup[0]]
    print('unfinished0 =', unfinished)
    best = Chain(0,(),0)
    while unfinished:
        c = unfinished.pop()
        while True: # build a full chain, putting the partial chains on the unfinished stack
            nextParts = [p for p in partlookup[c.port] if p not in c.seq]
            if not nextParts: # finished a sequence
                global sequences
                sequences += 1
                if c.val > best.val:
                    best = c
                    print(len(unfinished), 'unfinished, best',best,
                          orderSeq(best.seq), sum(sum(parts[i]) for i in best.seq))
                break
            else:
                n = nextParts.pop()
                c = inc(c,n)
                unfinished.extend(inc(c,p) for p in nextParts)

build()
print(sequences,'sequences tried')
