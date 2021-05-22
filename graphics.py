import os
import numpy as np
from PIL import Image
from random import shuffle

#SETTINGS

WIDTH=500
HEIGHT=50
INDIVIDUALWIDTH=int(WIDTH/HEIGHT)

notColor=[255, 255, 255, 255]
yesColor=[0, 0, 0, 255]
specialColor=[255, 0, 0, 255]

COLORWHEEL=notColor+yesColor+specialColor

heightList=[i for i in range(HEIGHT)]
shuffle(heightList)

print(heightList)
workingIndex=5

FRAMES=1
FPS=1
MAKE_VIDEO=False

#CODE

# from settings import *
# from sorting import *


class Graphics:
    @staticmethod
    def __drawNumberV(xIndex, heightList, pixels, colorWheel, workingIndex):

        #Goes through all y values
        for yValue in range(HEIGHT):

            #if it is in the bar
            print(xIndex, yValue, heightList[xIndex])
            if yValue < heightList[xIndex]:

                #if it is not what just got sorted
                if workingIndex*INDIVIDUALWIDTH > xIndex or (workingIndex+1)*INDIVIDUALWIDTH <= xIndex:
                    pixels[xIndex][yValue]=colorWheel[4], colorWheel[5], colorWheel[6], colorWheel[7]
    
                else:
                    pixels[xIndex][yValue]=colorWheel[8], colorWheel[9], colorWheel[10], colorWheel[11]

            #if it is not in the bar
            else:
                pixels[xIndex][yValue]=colorWheel[0], colorWheel[1], colorWheel[2], colorWheel[3]

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
    def __image(heightList, workingIndex, colorWheel, frame):

        pixels=np.ndarray( ( WIDTH, WIDTH, 4) )

        pixels = Graphics.__drawAllNumbersV(heightList, pixels, colorWheel, workingIndex)

        # print(frame/FRAMES)

        # print(pixels)
        image = Image.fromarray(np.uint8(pixels)).convert('RGB')
        image  = image.rotate(90)
        image2 = image.crop((0, WIDTH-HEIGHT, WIDTH, WIDTH))

        image2.save("./data/{}cropped.png".format(frame))
        image.save("./data/{}.png".format(frame))


        #TODO: Integrate Edward's Code
        # heightList, workingIndex = Calculate.__drawAllNumbersV(heightList, workingIndex)

        return heightList, workingIndex

    @staticmethod 
    def createVideo(heightList, workingIndex):

        for frame in range(FRAMES):

            heightList, workingIndex = Graphics.__image(heightList, workingIndex, COLORWHEEL, frame)

        if MAKE_VIDEO:
            os.system("ffmpeg -framerate {} -start_number 1 -i ./data/%d.png {}.mov".format(FPS, VIDEO_NAME))

if __name__ == '__main__':
    Graphics.createVideo(heightList, workingIndex)