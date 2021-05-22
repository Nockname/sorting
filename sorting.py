import copy
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
    def insertionSort(inputList, workIndex, BOOKMARK):

        done=False
        changed=[]

        if BOOKMARK==-1:
            done=True
            return inputList, workIndex, BOOKMARK, done, changed

        inputCopy=copy.deepcopy(inputList)

        # print(inputList)

        if inputList[workIndex]>inputList[workIndex+1]:
            # print("SWAP")

            inputCopy[workIndex]=inputList[workIndex+1]
            inputCopy[workIndex+1]=inputList[workIndex]

            changed.extend([workIndex, workIndex+1])

            if workIndex < len(inputList) - 2:

                workIndex+=1

            else:

                BOOKMARK-=1
                workIndex=BOOKMARK

                if workIndex not in changed:
                    changed.append(workIndex)
                

        else:
            BOOKMARK-=1

            changed.extend([workIndex, BOOKMARK])

            workIndex=BOOKMARK

        return inputCopy, workIndex, BOOKMARK, done, changed