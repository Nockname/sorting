from math import pi
import os
import numpy as np
from PIL import Image
from sorting import *
from settings import *
import copy


if method=="insertion":
    workingIndex=[int(WIDTH-2), int(WIDTH-2)]
else:
    workingIndex=[0, -1]


class Graphics:
    @staticmethod
    def __drawColumn(xIndex, heightList, pixels, colorWheel, workingIndex):

        #Not part of line
        for yValue in range(heightList[xIndex], HEIGHT):

            pixels[HEIGHT-1-yValue][xIndex]=colorWheel[0]

        #Special1
        if workingIndex[0] == xIndex:

            for yValue in range(0, heightList[xIndex]):

                pixels[HEIGHT-1-yValue][xIndex]=colorWheel[2]

            return pixels

        #Special 2
        if workingIndex[1] == xIndex:
    
            for yValue in range(0, heightList[xIndex]):

                pixels[HEIGHT-1-yValue][xIndex]=colorWheel[3]

            return pixels
    
        #Part of Line
        for yValue in range(0, heightList[xIndex]):

            pixels[HEIGHT-1-yValue][xIndex]=colorWheel[1]

        return pixels

    @staticmethod
    def __drawAllColumns(heightList, workingIndex, pixels, colorWheel, changedIndexes):

        #Go through all columns
        for xValue in changedIndexes:
            
            if xValue >= WIDTH:
                continue

            #Set the colors for that colum
            pixels = Graphics.__drawColumn(xValue, heightList, pixels, colorWheel, workingIndex)

        return pixels

    @staticmethod
    def __image(heightList, workingIndex, colorWheel, frame, lastPixels):

        if method == "bubble":
            heightList, workingIndex = Sorting.bubbleSort(heightList, workingIndex)
        if method == "insertion":
            heightList, workingIndex, done, changesColumns = Sorting.insertionSort(heightList, workingIndex)

        pixels = Graphics.__drawAllColumns(heightList, workingIndex, lastPixels.copy(), colorWheel, changesColumns)

        image = Image.fromarray(np.uint8(pixels)).convert('RGB')
        image = image.resize((TOTALWIDTH, HEIGHT))

        image.save("./data/{}.png".format(frame))

        print(frame/FRAMES, changesColumns)


        return heightList, workingIndex, done, pixels

    @staticmethod 
    def createVideo(heightList, workingIndex):

        done=False

        basicPixels=np.ndarray( ( HEIGHT, WIDTH, 4) )

        for yValue in range(HEIGHT):
            for xValue in range(WIDTH):
                basicPixels[yValue][xValue]=[255, 255, 255, 255]

        basicPixels = Graphics.__drawAllColumns(heightList, workingIndex, basicPixels, COLORWHEEL, [i for i in range(WIDTH)])

        for frame in range(FRAMES):
            if not done:
                heightList, workingIndex, done, basicPixels = Graphics.__image(heightList, workingIndex, COLORWHEEL, frame, basicPixels)


        if MAKE_VIDEO:
            os.system("ffmpeg -framerate {} -start_number 1 -i ./data/%d.png -vcodec libx264 -pix_fmt yuv420p {}.mov".format(FPS, VIDEO_NAME))
            os.system("open sort.mov")

if __name__ == '__main__':
    lastPixels=np.ndarray( ( HEIGHT , WIDTH, 4) )
    Graphics.createVideo(heightList, workingIndex)