# reference: https://www.cnblogs.com/wj-1314/p/9472962.html

import cv2 as cv
import numpy as np
from PIL import Image

ifd = 'ptest.jpg'
ofd = 'output.jpg'
lena = 'lena.bmp'

img = cv.imread(lena)

print(img)
print('the original shape is:', img.shape)
print('the original dimensions:', img.ndim)

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 

print(gray_img)
print('the gray shape is:', gray_img.shape)
print('the gray dimensions:', gray_img.ndim)

# have a try
# print('note:', img[[0,0],[0,1],[0,1]])

sumnum = 0.0
# for x in np.nditer(img):
#    print(x, end=' ')

def traverse_3d_pixels(img):
    height = img.shape[0]
    width = img.shape[1]
    channels = img.shape[2]
    for row in range(height):
        for col in range(width):
            for channel in range(channels):
                print(img[row][col][channel])

# traverse_3d_pixels(img)

def traverse_2d_pixels(img, sumnum):
    height = img.shape[0]
    width = img.shape[1]
    for row in range(height):
        for col in range(width):
            print(img[row][col])
            sumnum += img[row][col]
    print('sum', sumnum)

traverse_2d_pixels(gray_img, sumnum)

cv.imwrite(ofd, img)
