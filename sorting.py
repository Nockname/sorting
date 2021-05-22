import copy

from numpy import append
from settings import *

class Sorting:
    @staticmethod
    def bubbleSort(inputList, workIndex):

        inputCopy=copy.deepcopy(inputList)

        # print(inputList)

        if inputList[workIndex]>inputList[workIndex+1]:
            # print("SWAP")

            inputCopy[workIndex]=inputList[workIndex+1]
            inputCopy[workIndex+1]=inputList[workIndex]

        if workIndex < len(inputList) - 2:

            workIndex+=1

        else:

            workIndex=0

        # print(inputCopy)

        return inputCopy, workIndex

    @staticmethod
    def insertionSort(inputList, workIndex):

        done=False
        changed=[]

        if workIndex[1]==-1:
            done=True
            return inputList, workIndex, done, changed

        inputCopy=copy.deepcopy(inputList)

        if inputList[workIndex[0]]>inputList[workIndex[0]+1]:

            inputCopy[workIndex[0]]=inputList[workIndex[0]+1]
            inputCopy[workIndex[0]+1]=inputList[workIndex[0]]

            changed.extend([workIndex[0], workIndex[0]+1])

            if workIndex[0] < len(inputList) - 2:

                workIndex[0]+=1

            else:

                workIndex[1]-=1
                workIndex[0]=workIndex[1]

                if workIndex[0] not in changed:
                    changed.append(workIndex[0])

        else:
            workIndex[1] -= 1

            changed.extend([workIndex[0], workIndex[1]])
            workIndex[0] = workIndex[1]

        return inputCopy, workIndex, done, changed