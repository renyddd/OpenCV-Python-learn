import cv2 as cv
import numpy as np

ifd = 'lena.bmp'
ifd = 'me.jpg'
ofd1 = 'output.jpg'
ofd2 = 'ptest1.jpg'
ofd3 = 'ptest2.jpg'
img = cv.imread(ifd)

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
print(type(gray_img))
print(gray_img.shape)

# https://blog.csdn.net/sunny2038/article/details/9097989
b, g, r = cv.split(img)

def calcAndDrawHist(img, color):
    hist = cv.calcHist([img], [0], None, [256], [0.0,255.0])
    minVal, maxVal, minLoc, maxLoc = cv.minMaxLoc(hist)
    histImg = np.zeros([256,256,3], np.uint8)
    hpt = int(0.9 * 256)

    for h in range(256):
        intensity = int(hist[h] * hpt / maxVal)
        cv.line(histImg, (h,256), (h,256-intensity), color)

    return histImg

hb = calcAndDrawHist(b, [255, 0, 0])
hg = calcAndDrawHist(g, [0, 255, 0])
hr = calcAndDrawHist(r, [0, 0, 255])

cv.imwrite(ofd1, img)
cv.imwrite(ofd1, hb)
cv.imwrite(ofd2, hg)
cv.imwrite(ofd3, hr)
