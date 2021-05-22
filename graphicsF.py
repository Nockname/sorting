import os
import numpy as np
from PIL import Image
from sorting import *
from settings import *
import copy


if method=="insertion":
    workingIndex=int(WIDTH/INDIVIDUALWIDTH-2)
else:
    workingIndex=0
BOOKMARK=workingIndex


class Graphics:
    @staticmethod
    def __drawNumberV(xIndex, heightList, pixels, colorWheel, workingIndex):
        
        # for yValue in range(heightList[xIndex]):

        #         if workingIndex*INDIVIDUALWIDTH > xIndex or (workingIndex+1)*INDIVIDUALWIDTH <= xIndex:

        #             pixels[HEIGHT-1-yValue][xIndex]=colorWheel[4], colorWheel[5], colorWheel[6], colorWheel[7]

        #         else:

        #             pixels[HEIGHT-1-yValue][xIndex]=colorWheel[8], colorWheel[9], colorWheel[10], colorWheel[11]

        # for yValue in range(heightList[xIndex], HEIGHT):
        #     pixels[HEIGHT-1-yValue][xValue]=colorWheel[0], colorWheel[1], colorWheel[2], colorWheel[3]

        for yValue in range(HEIGHT):

            if yValue < heightList[xIndex]:

                if workingIndex*INDIVIDUALWIDTH > xIndex or (workingIndex+1)*INDIVIDUALWIDTH <= xIndex:

                    pixels[HEIGHT-1-yValue][xIndex]=colorWheel[4], colorWheel[5], colorWheel[6], colorWheel[7]

                else:

                    pixels[HEIGHT-1-yValue][xIndex]=colorWheel[8], colorWheel[9], colorWheel[10], colorWheel[11]

            else:
                pixels[HEIGHT-1-yValue][xIndex]=colorWheel[0], colorWheel[1], colorWheel[2], colorWheel[3]

        return pixels

    @staticmethod
    def __drawAllNumbersV(heightList, workingIndex, pixels, colorWheel, changedIndexes):

        beefyHeight=[]
        for number in heightList:
            for _ in range(INDIVIDUALWIDTH):
                beefyHeight.append(number)

        #Go through all columns
        for xNotBeefy in changedIndexes:
            for xValue in range(xNotBeefy*INDIVIDUALWIDTH, xNotBeefy*INDIVIDUALWIDTH+INDIVIDUALWIDTH):
                if xValue>=WIDTH:
                    continue
                #Set the colors for that colum
                pixels=Graphics.__drawNumberV(xValue, beefyHeight, pixels, colorWheel, workingIndex)

        return pixels

    @staticmethod
    def __image(heightList, workingIndex, colorWheel, frame, BOOKMARK, lastPixels):



        if method == "bubble":
            heightList, workingIndex = Sorting.bubbleSort(heightList, workingIndex)
        if method == "insertion":
            heightList, workingIndex, BOOKMARK, done, changesColumns = Sorting.insertionSort(heightList, workingIndex, BOOKMARK)

        pixels = Graphics.__drawAllNumbersV(heightList, workingIndex, lastPixels.copy(), colorWheel, changesColumns)

        image = Image.fromarray(np.uint8(pixels)).convert('RGB')

        image.save("./data/{}.png".format(frame))

        print(frame/FRAMES, changesColumns)


        return heightList, workingIndex, BOOKMARK, done, pixels

    @staticmethod 
    def createVideo(heightList, workingIndex, BOOKMARK):

        done=False

        basicPixels=np.ndarray( ( HEIGHT, WIDTH, 4) )
        for yValue in range(HEIGHT):
            for xValue in range(WIDTH):
                basicPixels[yValue][xValue]=[255, 255, 255, 255]
        basicPixels = Graphics.__drawAllNumbersV(heightList, workingIndex, basicPixels, COLORWHEEL, [i for i in range(WIDTH)])

        for frame in range(FRAMES):
            if not done:
                heightList, workingIndex, BOOKMARK, done, basicPixels = Graphics.__image(heightList, workingIndex, COLORWHEEL, frame, BOOKMARK, basicPixels)


        if MAKE_VIDEO:
            os.system("ffmpeg -framerate {} -start_number 1 -i ./data/%d.png -vcodec libx264 -pix_fmt yuv420p {}.mov".format(FPS, VIDEO_NAME))
            os.system("open sort.mov")

if __name__ == '__main__':
    lastPixels=np.ndarray( ( HEIGHT , WIDTH, 4) )
    Graphics.createVideo(heightList, workingIndex, BOOKMARK)