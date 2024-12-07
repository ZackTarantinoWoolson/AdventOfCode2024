import os
import sys
import itertools


def runPermutations(data,ops):
    perms=[]
    operators=list(itertools.product(ops,repeat=len(data)-2))
    for o in operators:
        total=data[1]
        for i,e in enumerate(o,1):
            if e=="*":
                total *= data[i+1]
            elif e=="+":
                total += data[i+1]
            elif e=="|":
                total = int(str(total)+""+str(data[i+1]))
        if total==data[0]:
            perms.append(o)

    return len(perms)>0

data=[]
with open(os.path.join(os.path.dirname(sys.argv[0]), "input.txt"),"r") as file:
    for line in file:
        line = line.strip('\n')
        line = line.replace(":","")
        data.append(line.split())

for d in data:
    for i in range(len(d)):
        d[i]=int(d[i])

part1=0
part2=0

for d in data:
    validOperations,validEquation=runPermutations(d, "+*")
    if validEquation:
        part1+=d[0]

for d in data:
    validOperations,validEquation=runPermutations(d, "+*|")
    if validEquation:
        part2+=d[0]

print("Part 2: ", part2)