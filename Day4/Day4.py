import os
import sys
import re

def checkHorizontal(fullWordSeach):
    total=0
    for line in fullWordSeach:
        total+=len(re.findall("XMAS",''.join(line)))
        total+=len(re.findall("SAMX",''.join(line)))
    return total

def checkVertical(fullWordSeach):
    rotated = list(zip(*fullWordSeach[::-1]))
    return checkHorizontal(rotated)

def getDiagonalMatrix(n, m, li):
    row=[]
    rowReverse=[]

    # this first loop searchs diags like /
    ctr = 0
    while(ctr < 2 * n-1): # n=140, so ctr < 279
        lst = []
        for i in range(m): # m=140
            for j in range(n): # n=140
                # create list of diagonal elements
                if i + j == ctr:
                    lst.append(li[i][j])

        row.append(lst) # add list of diag elements to master array
        ctr += 1

    reversedArray=[]
    for line in li: # reverse the lines to search from the other side
        line.reverse()
        reversedArray.append(line)

    # this second loop searchs diags like \
    ctr = 0
    while(ctr < 2 * n-1):
        lst = []
        for i in range(m):
            for j in range(n):
                if i + j == ctr:
                    lst.append(reversedArray[i][j])

        rowReverse.append(lst)
        ctr += 1

    return row,rowReverse

def checkDiagonal(fullWordSeach):
    total=0
    mat1,mat2=getDiagonalMatrix(len(fullWordSeach),len(fullWordSeach),fullWordSeach)
    total+=checkHorizontal(mat1)
    total+=checkHorizontal(mat2)
    
    return total

def getX(x,y,fullWordSeach):
    xSearch=[]
    xSearch.append(fullWordSeach[x-1][y-1]+""+fullWordSeach[x][y]+""+fullWordSeach[x+1][y+1])
    xSearch.append(fullWordSeach[x+1][y-1]+""+fullWordSeach[x][y]+""+fullWordSeach[x-1][y+1])

    return xSearch

def checkDiagonalPart2(fullWordSeach):
    total=0

    for x,row in enumerate(fullWordSeach):
        if x==0 or x==(len(fullWordSeach)-1): continue # skip first and last row
        for y,letter in enumerate(row):
            if y==0 or y==(len(row)-1): continue # skip first and last col
            xsearch=getX(x,y,fullWordSeach)
            if (xsearch[0]== "SAM" or xsearch[0]== "MAS") and (xsearch[1]== "SAM" or xsearch[1]== "MAS"):
                total+=1

    return total

def setArray(line):
    parsed = re.findall("X|M|A|S",line)
    return parsed
        
part1=0
part2=0
fullWordSeach=[]

with open(os.path.join(os.path.dirname(sys.argv[0]), "input.txt"),"r") as file:
    for line in file:
        fullWordSeach.append(setArray(line))

part1+=checkHorizontal(fullWordSeach)
part1+=checkVertical(fullWordSeach)
part1+=checkDiagonal(fullWordSeach)

# fix reversal
for line in fullWordSeach: line.reverse()

part2+=checkDiagonalPart2(fullWordSeach)

print("Part 1:",part1, "   |   Part 2:",part2)