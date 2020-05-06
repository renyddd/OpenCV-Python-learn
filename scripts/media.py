import cv2 as cv        
import numpy as np      
import matplotlib.pyplot as plt
# reference - https://www.cnblogs.com/lfri/p/10627595.html


ifd1 = 'input.jpg' # dayanta
ofd = 'output.jpg'


def read_gray_img(fd):
    img = cv.imread(fd)    
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)    
    return img


import numpy as np
import random


def salt_noise(image,prob): # 0.03
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output
    

def gasuss_noise(img):
    res = np.copy(img)
    row, col = res.shape

    for i in range(5000):
        x = np.random.randint(0, row)
        y = np.random.randint(0, col)
        res[x, y] = 255  

    return res

def get_unique_without0(lst):
    data = lst.flatten()
    res = np.unique(data)
    data = np.sort(res)
    if 0 in data:
        data = data[1:]

    print(data)
    if len(data) == 0:
        return 0
    else:
        return data


def median_manual(img, choice):
    operator1 = np.array([[0, 0, 0],
                          [1, 1, 1],
                          [0, 0, 0]])
    operator2 = np.array([[0, 1, 0],
                         [1, 1, 1],
                         [0, 1, 0]])
    operator3 = np.array([[1, 1, 1],
                         [1, 1, 1],
                         [1, 1, 1]])
    
    pad = np.pad(img, (1,1), mode='constant', constant_values=0)
    r, c = pad.shape
    out = np.copy(pad)

    if choice == 'h1':
        choice = operator1
    elif choice == 'h2':
        choice = operator2
    elif choice == 'h3':
        choice = operator3
    else:
        return None

    for i in range(1, r-1):
        for j in range(1, c-1):
            data = choice * pad[i-1:i+2, j-1:j+2]
            R = np.median(get_unique_without0(data))
            out[i, j] = int(R)

    out = out[1:r-1, 1:c-1]
    cv.imwrite('output.jpg', out)


def median_official(img):
    media = cv.medianBlur(img, 3)
    cv.imwrite('ptest2.jpg', media)
    # 官方效果对比



def main():
    img = read_gray_img(ifd1)
    oimg = salt_noise(img, 0.03)
    cv.imwrite('ptest1.jpg', oimg)

    median_manual(oimg, 'h2')


    median_official(oimg)
    


if __name__ == "__main__":
    main()
