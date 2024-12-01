import os
import sys
from collections import Counter

leftList = []
rightList= []

with open(os.path.join(os.path.dirname(sys.argv[0]), "input.txt"),"r") as file:
    for line in file:
        x=line.split("   ")
        leftList.append(int(x[0]))
        rightList.append(int(x[1].replace("\n", "")))

leftList.sort()
rightList.sort()
total=0
simScoreTotal=0
countedList = Counter(rightList)

for index,item in enumerate(leftList):
    total+= abs(leftList[index]-rightList[index])
    simScoreTotal+=(item* countedList.get(item,0))

print("Part One:" , total)
print("Part Two:" , simScoreTotal)
