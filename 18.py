#! /usr/local/bin/python3

def hello(x):
    def f():
        print(x)
    return f

instructions = [hello("hi"), hello("there")]

for i in instructions:
    i()

