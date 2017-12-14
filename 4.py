#! /usr/local/bin/python3

valids = 0
while True: 
    line = input()
    if not line:
        print(valids, " valid passphrases")
        break
    if len(line.split()) == len(set(line.split())):
        valids += 1
    
