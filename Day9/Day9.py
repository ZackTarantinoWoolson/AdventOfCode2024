import os
import sys
import time
import copy

start_time = time.time()

def createDict(inputList):
    idCounter=0
    files={}
    for i in range(0,len(inputList),2):
        block=int(inputList[i])
        try:
            freespace=int(inputList[i+1])
        except:
            freespace=0
        files[idCounter]={}
        files[idCounter]["block"]=block
        files[idCounter]["freespace"]=freespace

        idCounter+=1

    printLine=""
    dataArray=[]
    for id in files:
        printLine+=""+(str(id)*files[id]["block"])+"."*files[id]["freespace"]
        for _ in range(files[id]["block"]):
            dataArray.append(id)
        for _ in range(files[id]["freespace"]):
            dataArray.append(".")

    return files,dataArray

# checks if everything to the right is a . - if so, nothing left to do
def checkIfDefagDone(index,dataArray):
    while index<len(dataArray):
        if dataArray[index]!=".":
            return False
        index+=1
    return True

def checksum(dataArray):
    checkSumTotal=0
    for index,d in enumerate(dataArray):
        if d==".": continue  # skip iterating after all ids are added

        checkSumTotal+=(index*d)
        # print(index,d,checkSumTotal)
    return checkSumTotal


def defragPartOne(origArray):
    dataArray=copy.deepcopy(origArray) #make a copy to manipulate
    pointer1=0
    pointer2=len(dataArray)-1
    
    # while the head pointer has not made it to the end of the array
    while pointer1<len(dataArray):
        if checkIfDefagDone(pointer1,dataArray): break 

        if str(dataArray[pointer1])!=".": #if the head pointer is not at free space, move on
            pointer1+=1
            continue
        if str(dataArray[pointer2])==".": #if the end of the list has a ., move head pointer back and end pointer forward
            pointer1-=1
            pointer2-=1
            continue

        # swap file block with freespace
        dataArray[pointer1],dataArray[pointer2]=dataArray[pointer2],dataArray[pointer1]

        pointer1+=1
    return dataArray


# look for where in the data array there is a sub-array of enough free spaces
def find_slice_index(array, subarray):
    for i in range(len(array) - len(subarray) + 1):
        if array[i:i + len(subarray)] == subarray:
            return i
    return -1  # Return -1 if no match found

def defragPartTwo(files,origArray):
    dataArray=copy.deepcopy(origArray)

    # pointers for the dict
    pointer1=0
    pointer2=len(files)-1

    # pointers for the list
    arrayPointer1=files[0]["block"]
    arrayPointer2=len(dataArray)

    while pointer1<len(files):

        # if the dict pointer reaches 0, we have checked all of the file blocks
        if pointer2==0:
            break

        # if the head pointer meets or tries to go past the end pointer, reset and try the next rightmost file block
        if pointer1>=pointer2:
            pointer1=0
            pointer2-=1
            continue

        # if there is available freespace for the last block
        if files[pointer2]["block"]<=files[pointer1]["freespace"]: 

            # look for the leftmost available spot
            arrayPointer1 = find_slice_index(dataArray, ['.']*files[pointer2]["block"])
            if arrayPointer1 == -1:
                print("actually not enought space somehow ", arrayPointer1)
                exit(1)

            # grab the index of the start of the file block
            arrayPointer2 = dataArray.index(pointer2)+files[pointer2]["block"]
            
            # swap the file block with the found leftmost freespace
            dataArray[arrayPointer1:arrayPointer1+files[pointer2]["block"]],dataArray[arrayPointer2-files[pointer2]["block"]:arrayPointer2]=dataArray[arrayPointer2-files[pointer2]["block"]:arrayPointer2],dataArray[arrayPointer1:arrayPointer1+files[pointer2]["block"]]

            #remove the amount of available freespace by the block usage
            files[pointer1]["freespace"]-=files[pointer2]["block"] 

            pointer1=0 #reset head pointer
            pointer2-=1 #iterate end pointer
            continue

        pointer1+=1 # if there was no freespace available, check the next block
        
    return dataArray

part1=0
part2=0
inputList=[]

with open(os.path.join(os.path.dirname(sys.argv[0]), "input.txt"),"r") as file:
    for line in file:
        for c in line:
            inputList.append(c)
        

filesDict,dataArray=createDict(inputList)
part1=checksum(defragPartOne(dataArray))

part1Time=(time.time()-start_time)*1000
print("\n\nPart 1:",part1)
print("Total elapsed time for Part 1: %.2f ms" % (part1Time))

part2Start= time.time()
part2=checksum(defragPartTwo(filesDict,dataArray))

part2Time=(time.time()-part2Start)
print("\n\nPart 2:",part2)
print("Total elapsed time: %.2f s" % (part2Time))