import os
import sys
import re

skip = False

def test(line):
    parsed = re.findall("mul\(\d+,\d+\)",line)
    total=0
    for x in parsed:
        numbers=re.findall("\d+",x)
        total+=(int(numbers[0])*int(numbers[1]))
    return total

def test2(string):
    parsed = re.findall("mul\(\d+,\d+\)|don't\(\)|do\(\)",string)
    total=0
    for x in parsed:
        global skip
        
        if x=="don't()": skip=True   
        elif x=="do()":
            skip=False
            continue
        if skip: continue

        numbers=re.findall("\d+",x)
        total+=(int(numbers[0])*int(numbers[1]))
    return total
        
part1=0
part2=0

with open(os.path.join(os.path.dirname(sys.argv[0]), "input.txt"),"r") as file:
    for line in file:
        # print(line)
        part1+=test(line)
        part2+=test2(line)

print("Part 1:",part1, "   |   Part 2:",part2)