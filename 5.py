#! /usr/local/bin/python3

xs = []

def jump(i, xs):
    s = 0
    while 0 <= i < len(xs):
        s += 1
        xs[i] += 1
        i += xs[i] - 1
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


