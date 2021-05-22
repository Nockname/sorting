from settings import *
import os

os.system("ffmpeg -framerate {} -start_number 1 -i ./data/%d.png -vcodec libx264 -pix_fmt yuv420p {}.mov".format(FPS, VIDEO_NAME))
os.system("open sort.mov")