from random import shuffle

WIDTH=500
TOTALWIDTH=2000
HEIGHT=1000
INDIVIDUALWIDTH=4


BOOKMARK=0

method="insertion"

notColor=[255, 255, 255, 255]
yesColor=[0, 0, 0, 255]
specialColor=[255, 0, 0, 255]
specialColor2=[255, 255, 0, 255]

COLORWHEEL=[notColor]+[yesColor]+[specialColor]+[specialColor2]

heightList=[i+1 for i in range(0, HEIGHT, int(HEIGHT/WIDTH))]

shuffle(heightList)

FRAMES=100000
FPS=60
MAKE_VIDEO=True
VIDEO_NAME="sort"