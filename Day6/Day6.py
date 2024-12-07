import os
import sys


# Part 1: 5531
# Part 2: 2165

def findStartingArea(map):
    for y,r in enumerate(map):
        if "^" in r:
            return [r.index("^"),y]

def nextDirection(direction):
    if direction=="up":
        return "right"
    elif direction=="right":
        return "down"
    elif direction=="down":
        return "left"
    elif direction=="left":
        return "up"


def walkUntilObject(map,currentPos,direction):
    # print("current position:  ", currentPos)
    global distinctPositions
    if direction=="up":
        for y in range(currentPos[1],-1,-1):
            # print(y, map[y][currentPos[0]])
            if map[y][currentPos[0]] == "#":
                break
            else:
                if y==currentPos[1]: continue
                distinctPositions.append([currentPos[0],y])
                map[y][currentPos[0]]="^"
    elif direction=="right":
        for x in range(currentPos[0],len(map[currentPos[1]])+1,1):
            # print(x, map[currentPos[1]][x])
            if map[currentPos[1]][x] == "#":
                break
            else:
                if x==currentPos[0]: continue
                distinctPositions.append([x,currentPos[1]])
                map[currentPos[1]][x]=">"
    elif direction=="down":
        for y in range(currentPos[1],len(map)+1,1):
            # print(y, map[y][currentPos[0]])
            if map[y][currentPos[0]] == "#":
                break
            else:
                if y==currentPos[1]: continue
                distinctPositions.append([currentPos[0],y])
                map[y][currentPos[0]]="v"
    elif direction=="left":
        for x in range(currentPos[0],-1,-1):
            # print(x, map[currentPos[1]][x])
            if map[currentPos[1]][x] == "#":
                break
            else:
                if x==currentPos[0]: continue
                distinctPositions.append([x,currentPos[1]])
                map[currentPos[1]][x]="<"
    


    return currentPos

map=[]
distinctPositions=[]


with open(os.path.join(os.path.dirname(sys.argv[0]), "input.txt"),"r") as file:
    for line in file:
        map.append(list(line.strip('\n')))


distinctPositions.append(findStartingArea(map))
start=findStartingArea(map)
# for p in distinctPositions:
#     print(map[p[1]][p[0]])

direction="up"

run=True
while run:
    # print(run, direction)
   
    # print(distinctPositions[-1],direction)
    try: 
        walkUntilObject(map,distinctPositions[-1],direction)
        # print(distinctPositions[-1])
        map[distinctPositions[-1][1]][distinctPositions[-1][0]]="@"
        if distinctPositions[-1][0]==0 or distinctPositions[-1][0]==len(map[0]) or distinctPositions[-1][1]==0 or distinctPositions[-1][1]==len(map):
            # print("HEREHER")
            run=False
    except:
        break
    # for m in map:
    #     print(''.join(m))
    direction=nextDirection(direction)
    # print(distinctPositions)
    # break



print("\n\n ====END MAP==== \n\n")
map[start[1]][start[0]]="?"
for m in map:
    print(''.join(m))

# print(distinctPositions)
# 1920 too low.. 

# distinctPositions=set(distinctPositions)

stringifyList=[]
for i,d in enumerate(distinctPositions):
    stringifyList.append(""+str(d[0])+","+str(d[1]))

uniqSet=set(stringifyList)


print("Part 1:",len(uniqSet))