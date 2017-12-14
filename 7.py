#! /usr/local/bin/python3

# run as: ./7.py < 7.input.txt
from collections import defaultdict
import re

children = defaultdict(list)
father = defaultdict()
weight = dict()

while True:
    # https://stackoverflow.com/a/42891677/268040
    try:
        line = input()
    except EOFError:
        break
    if not line:
        break
    name, w, *cs = re.split('\s+->\s+|,?\s+', line)
    weight[name] = int(w.strip('()'))
    # print("name =", name, ", weight", w, ", children =", cs)
    if cs:
        for c in cs:
            father[c] = name
            children[name].append(c)

root, = set(children.keys()) - set(father.keys())
print("name with no father is:", root)
weights = defaultdict(int)
def getWeights(p):
    weights[p] += weight[p]
    for c in children[p]:
        weights[p] += getWeights(c)
    return weights[p]
    
print("root weight =", getWeights(root))

def isUnbalanced(n):
    if n not in children or len(children[n]) == 0:
        return False
    w = weights[children[n][0]]
    return any([w!=weights[c] for c in children[n]])

def traceUnbalanced(p):
    if p in children and len(children[p]) > 0:
        cweights = [weights[c] for c in children[p]]
        u = min(children[p], key=lambda c: cweights.count(weights[c]))
        if isUnbalanced(u):
            print("At node", p, "node", u, "is unbalanced", [(c,weights[c]) for c in children[p]])
            traceUnbalanced(u)
        else:
            correctWeight = max(cweights, key=lambda w: cweights.count(w))
            print("Node", u, "should weigh", correctWeight - (weights[u]-weight[u]), "not", weight[u])
        

traceUnbalanced(root)

