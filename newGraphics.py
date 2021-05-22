import os
import numpy as np
from PIL import Image
from sorting import *
from settings import *
import copy

basicPixels=np.ndarray( ( HEIGHT, WIDTH, 4) )

for xValue in range(HEIGHT):
    for yValue in range(WIDTH):
        basicPixels[xValue][yValue]=[255, 255, 255, 255]


if method=="insertion":
    workingIndex=HEIGHT-2
else:
    workingIndex=0

BOOKMARK=workingIndex
class Graphics:
    @staticmethod
    def __drawNumberV(xIndex, heightList, pixels, colorWheel, workingIndex):

        #Goes through all y values
        if workingIndex*INDIVIDUALWIDTH > xIndex or (workingIndex+1)*INDIVIDUALWIDTH <= xIndex:
            for yValue in range(HEIGHT):

                #if it is in the bar
                if yValue < heightList[xIndex]:

                    pixels[HEIGHT-1-yValue][xIndex]=colorWheel[4], colorWheel[5], colorWheel[6], colorWheel[7]

                else:
                    break

        else:
            #Goes through all y values
            for yValue in range(HEIGHT):

                #if it is in the bar
                if yValue < heightList[xIndex]:

                    pixels[HEIGHT-1-yValue][xIndex]=colorWheel[8], colorWheel[9], colorWheel[10], colorWheel[11]

                else:
                    break

        return pixels

    @staticmethod
    def __drawAllNumbersV(heightList, pixels, colorWheel, workingIndex):

        beefyHeight=[]
        for number in heightList:
            for _ in range(INDIVIDUALWIDTH):
                beefyHeight.append(number)

        # print(beefyHeight)

        #Go through all columns
        for xValue in range(0, WIDTH):
            #Set the colors for that column
            pixels=Graphics.__drawNumberV(xValue, beefyHeight, pixels, colorWheel, workingIndex)

        return pixels

    @staticmethod
    def __image(heightList, workingIndex, colorWheel, frame, BOOKMARK):

        pixels=basicPixels.copy()

        pixels = Graphics.__drawAllNumbersV(heightList, pixels, colorWheel, workingIndex)

        print(frame/FRAMES)

        # print(pixels)
        image = Image.fromarray(np.uint8(pixels)).convert('RGB')

        image.save("./data/{}.png".format(frame))

        if method == "bubble":
            heightList, workingIndex = Sorting.bubbleSort(heightList, workingIndex)
        if method == "insertion":
            heightList, workingIndex, BOOKMARK, done = Sorting.insertionSort(heightList, workingIndex, BOOKMARK)

        return heightList, workingIndex, BOOKMARK, done

    @staticmethod 
    def createVideo(heightList, workingIndex, BOOKMARK):

        done=False

        for frame in range(FRAMES):
            if not done:
                heightList, workingIndex, BOOKMARK, done = Graphics.__image(heightList, workingIndex, COLORWHEEL, frame, BOOKMARK)


        if MAKE_VIDEO:
            os.system("ffmpeg -framerate {} -start_number 1 -i ./data/%d.png {}.mov".format(FPS, VIDEO_NAME))

if __name__ == '__main__':
    Graphics.createVideo(heightList, workingIndex, BOOKMARK)