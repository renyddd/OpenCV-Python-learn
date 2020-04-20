import cv2 as cv
import numpy as np

img = cv.imread('me.jpg')

def Beauty(img):
    value = 50
    img = cv.bilateralFilter(img, value, value * 2, value / 2)
    return img 

res = Beauty(img)
cv.imwrite('output.jpg', res)

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray_res = cv.cvtColor(res, cv.COLOR_BGR2GRAY)

fimg = np.float32(gray_img)                                                
fres = np.float32(gray_res)
# 只能对灰度图像进行 DCT 变化
# 一次对比美图对频域的影响
fimg_dct = cv.dct(fimg)
fres_dct = cv.dct(fres)

cv.imwrite('ptest1.jpg', fimg_dct)
cv.imwrite('ptest2.jpg', fres_dct)

# 从频域和时域查看去掉了什么东西
dimg = fimg_dct - fres_dct # 频域所差
# cv.imwrite('output.jpg', dimg)

dimg = cv.idct(dimg)
cv.imwrite('ptest1.jpg', dimg) # 时域所差
