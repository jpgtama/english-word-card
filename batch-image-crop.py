from PIL import Image
import os
import glob
from math import floor

srcFolder = "C:\\Users\\310199253\\Downloads\\9.英语单词\\"

outputFolder = "C:\\Users\\310199253\\Downloads\\9.英语单词-crop\\"

allImages = []

def scale(im):
    width, height = im.size
    newW = floor(width * 0.4)
    newH = floor(height * 0.4)
    im1 = im.resize((newW, newH))
    return im1

def paddingToA4(im):
    a4im = Image.new("RGB", (595, 842), (255, 255, 255))
    a4W, a4H = a4im.size
    w, h = im.size
    offset = ( (a4W - w)//2, (a4H-h)//2  )
    a4im.paste(im, offset)
    return a4im




for file in glob.glob(srcFolder + "*.jpg"):
    allImages.append(file)

for file in allImages:
    # print(os.path.basename(file))
    im = Image.open(file)
    width, height = im.size
    im1 = im.crop((0, 100, width, height-300))

    im2 = scale(im1)

    im3 = paddingToA4(im2)

    im3.save(outputFolder+os.path.basename(file))

