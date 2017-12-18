#! /usr/local/bin/python3

# run as: ./12.py < 12.input.txt
from collections import defaultdict
import re

connected = defaultdict(set)

while True:
    # https://stackoverflow.com/a/42891677/268040
    try:
        line = input()
    except EOFError:
        break
    if not line:
        print("No line")
        next
    x, *xs = map(int, re.split(', | <-> ', line))
    connected[x].update(xs)
    if x == 0: print("line:",line,"\nconnected[",x,"] = ", xs, "\n")

# print("connected[0]", connected[0])

groups = []
seen = set()
for root in connected:
    if root not in seen:
        g = set([root])
        q = [root]
        while len(q) > 0:
            root = q.pop(0)
            g.add(root)
            if root not in seen:
                q.extend(connected[root])
                seen.add(root)
        groups.append(g)
print("Group 0 has length", len(groups[0]))
print("The number of groups is", len(groups))
        
# q = [0]
# results = set([0])
# seen = set([0])
# while len(q) > 0:
#     x = q.pop(0)
#     print("working on", x, connected[x])
#     for k in connected[x]:
#         results.add(k)
#         if k not in seen:
#             q.append(k)
#             print("q", q)
#         seen.add(k)

# print(len(results))
        
    
        
