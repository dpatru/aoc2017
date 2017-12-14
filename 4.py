#! /usr/local/bin/python3

# run as ./4.py < 4.passPhrases.txt

valids = 0
while True: 
    line = input()
    if not line:
        print(valids, " valid passphrases")
        break
    # if len(line.split()) == len(set(line.split())): # part 1
    if len(line.split()) == len(set([tuple(sorted(w)) for w in line.split()])): # part 2
        valids += 1
    
