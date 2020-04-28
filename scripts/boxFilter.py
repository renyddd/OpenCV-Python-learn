import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
# reference:
#   laplace - https://www.webfalse.com/read/205084/1384493.html
#   laplaceoperator - https://www.jqhtml.com/48318.html
#   简化版 - https://www.cnblogs.com/iwuqing/p/11478583.html 
#   <++> 
#   <++> 
#   <++> 

ifd = 'lena.bmp'
ofd = 'output.jpg'
img = cv.imread(ifd)
gimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

row, col = gimg.shape

for i in range(5000):
    x = np.random.randint(0, row)
    y = np.random.randint(0, col)
    gimg[x, y] = 255

cv.imwrite('ptest1.jpg', gimg)

# box filter
res = cv.boxFilter(gimg, -1, (3,3), normalize=1)

# Gaussian
res = cv.GaussianBlur(gimg, (3,3), 0)
cv.imwrite('output.jpg', res)

# Laplacian
lap = cv.Laplacian(res, cv.CV_16S, ksize=3)
rlap = cv.Laplacian(gimg, cv.CV_16S, ksize=3)

# laplace_operator
laplace_operator = np.array([[0, 1, 0],
                            [1, -5, 1],
                            [0, 1, 0]])
lgimg = np.pad(gimg, (1,1), mode='constant', constant_values=0)
m, n = lgimg.shape
cv.imwrite('ptest1.jpg', lgimg)
out = np.copy(lgimg)
for i in range(1, m - 1):
    for j in range(1, n - 1):
        R = np.sum(laplace_operator * lgimg[i - 1:i + 2, j - 1:j + 2])
        out[i, j] = lgimg[i, j] + R
out = out[1:m - 1, 1:n - 1]
cv.imwrite('ptest1.jpg', out)


titles = ['p1', 'p2', 'p3', 'p4']
imgs = [gimg, res, out, rlap]
plt.figure()
for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(imgs[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.savefig(ofd)
