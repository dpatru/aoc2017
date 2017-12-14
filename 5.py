#! /usr/local/bin/python3

# run as: ./5.py < 5.input.txt

xs = []

def jump(i, xs):
    s = 0
    while 0 <= i < len(xs):
        s += 1
        j = xs[i]
        # xs[i] += 1 # increase the jump, part 1
        xs[i] += (1 if j < 3 else -1) # part 2
        i += j
        # print("i = ", i)
    return s

while True:
    # https://stackoverflow.com/a/42891677/268040
    try:
        line = input()
    except EOFError:
        break
    if not line:
        break
    xs.append(int(line))

print("number is ", jump(0, xs))


