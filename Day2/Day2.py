import os
import sys

def test(list):
    x=[int(y) for y in list]

    for index in range(len(x)-1):
    
        if abs(x[index]-x[index+1]) not in [1,2,3]:
            return False
        elif abs(x[index]-x[index+1]) == 0:
            return False

    increasing = all(x[index] < x[index+1] for index in range(len(x)-1))
    decreasing = all(x[index] > x[index+1] for index in range(len(x)-1))
    return increasing or decreasing


def test2(list):
    if (test(list)):
        return True
    
    for i in range(len(list)):
        new_list=list[:i]+list[i+1:]
        if test(new_list):
            return True

    return False
        

part1=0
part2=0

with open(os.path.join(os.path.dirname(sys.argv[0]), "input.txt"),"r") as file:
    for line in file:
        part1+=test(line.split()) #part1
        part2+=test2(line.split())

            
print("Part 1:",part1)
print("Part 2:",part2)
