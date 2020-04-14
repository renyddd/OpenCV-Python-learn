import cv2 as cv
import numpy as np
# from PIL import Image

lady = 'lady.bmp'
lena = 'lena.bmp'
ifd = lena
ofd = 'output.jpg'

img = cv.imread(ifd)
img1 = cv.imread(lena)
img2 = cv.imread(lady)


gray_img1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY) 
gray_img2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY) 

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
            # print(img[row][col])
            sumnum += img[row][col]
    # print('sum', sumnum)
    return sumnum

sum1 = 0.0
sum2 = 0.0

print('gray_img1:', gray_img1.shape)
sum1 = traverse_2d_pixels(gray_img1, sum1)
print('gray_img2:', gray_img2.shape)
sum2 = traverse_2d_pixels(gray_img2, sum2)

# 求灰度平均值
def gray_scale_mean_value(sumn):
    fba = sumn / 256 /256
    print('gray_scale_mean_value:', fba)
    return fba

fba1 = gray_scale_mean_value(sum1)
fba2 = gray_scale_mean_value(sum2)

# 求两幅灰度图像的协方差值，fba1 传给 f1 代表图一的灰度平均值
def covariance_value(f1, f2, i1, i2):
    cfg = 0.0
    height = i1.shape[0]
    width = i1.shape[1]
    for row in range(height):
        for col in range(width):
            cfg += (i1[row][col] - f1) * (i2[row][col] - f2)
    return (cfg / 256 / 256)

cfg = covariance_value(fba1, fba2, gray_img1, gray_img2)
print('convariance:', cfg)

# 使用 np 函数计算协方差：https://blog.csdn.net/theonegis/article/details/85059105
m1 = gray_img1.mean()
m2 = gray_img2.mean()
print('np mean1:', m1)
print('np mean2:', m2)
# np_cov = np.cov(gray_img1, gray_img2)
# print('np covariance:', np_cov)
# 上述计算协方差值不对，试着全部转化为一维矩阵，再计算协方差
c1 = gray_img1.flatten()
c2 = gray_img2.flatten()
# print('try cov:', c1, c2)
print('np cov matrix:', np.cov(c1, c2))
print('np cov value:', np.cov(c1, c2)[0,1]) # 取矩阵中 (0,1) 元素
# http://www.atyun.com/17363.html 获取到从 cov() 得到协方差值


# 计算图像的方差 variance
def variance(img):
    variance_value = 0.0
    mi = img.mean()
    ni = img.flatten()
    for item in ni:
        variance_value += (( item - mi ) ** 2)
    variance_value = variance_value / 256 / 256
    return variance_value

vari = variance(img)
print('variance of lena:', vari)


# 标准差
def stddev(variance_value):
    return variance_value ** 0.5

stdd = stddev(vari)
print('stddev of lena', stdd) 


# 计算相关系数
vari1 = variance(img1)
vari2 = variance(img2)
stdd1 = stddev(vari1)
stdd2 = stddev(vari2)
rfg = cfg / stdd1 / stdd2
print('rfg:', rfg)
coefxy = np.corrcoef(c1, c2)
# https://blog.csdn.net/zuliang001/article/details/82501934
print('np rfg matrix:', coefxy)
print('np rfg:', coefxy[0,1])

