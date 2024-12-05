import os
import sys

rules=[]
updates=[]

def checkIfY(update):
    global rules
    rulesToReturn=[]
    for rule in rules:
        if (update==rule[1]):
            rulesToReturn.append(rule)

    return rulesToReturn

def partOne(updates):
    for i,update in enumerate(updates):
        relevantRules=[]
        for r in checkIfY(update):
            if r[0] in updates: relevantRules.append(r)

        for r in relevantRules:
            if updates.index(r[0])>i: return False
            
    return True

def partTwo(updates):
    for i,update in enumerate(updates):
        relevantRules=[]
        for r in checkIfY(update):
            if r[0] in updates: relevantRules.append(r)

        if len(relevantRules) == len(updates)//2:
            return int(updates[i])

part1=0
part2=0

with open(os.path.join(os.path.dirname(sys.argv[0]), "input.txt"),"r") as file:
    endofRules=False
    for line in file:
        if line=='\n':
            endofRules=True
            continue
        if endofRules:
            updates.append(line.strip('\n').split(","))
            continue

        rules.append(line.strip('\n').split("|"))

for update in updates:
    if partOne(update):
        part1+=int(update[len(update)//2])
    else:
        part2+=partTwo(update)

print("Part 1:",part1, "   |   Part 2:",part2)