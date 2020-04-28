import cv2 as cv        
import numpy as np      
import matplotlib.pyplot as plt

ifd1 = 'input.jpg' # dayanta
ofd = 'output.jpg'      

def read_gray_img(fd):
    img = cv.imread(fd)    
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)    
    return img

def add_noise(img):
    res = np.copy(img)
    row, col = res.shape
    for i in range(5000):
        x = np.random.randint(0, row)
        y = np.random.randint(0, col)
        res[x, y] = 255  
    return res

def box_filter(img):
    res = cv.boxFilter(img, -1, (3,3), normalize=1)
    cv.imwrite('output.jpg', res)

def gaussian_filter(img):
    res = cv.GaussianBlur(img, (3,3), 0)
    cv.imwrite('output.jpg', res)

def laplace_filter(img):
    res = cv.Laplacian(img, cv.CV_16S, ksize=3)
    cv.imwrite('output.jpg', res)

def lap_manual(img, choice):
    laplace_operator1 = np.array([[0 ,-1, 0],
                                  [-1, 5, -1],
                                  [0, -1, 0]])
    laplace_operator2 = np.array([[-1, -1, -1],
                                  [-1, 9, -1],
                                  [-1, -1, -1]])
    if choice == 'h3':
        choice = laplace_operator1
    elif choice == 'h4':
        choice = laplace_operator2
    pad = np.pad(img, (1,1), mode='constant', constant_values=0)
    r, c = pad.shape
    out = np.copy(pad)
    for i in range(1, r-1):
        for j in range(1, c-1):
            R = np.sum(choice * pad[i-1:i+2, j-1:j+2])
            out[i, j] = pad[i, j] - R
    out = out[1:r-1, 1:c-1]
    cv.imwrite('output.jpg', out)

def choose_h(fd, choice):
    src = read_gray_img(fd)
    img = src # h1, h2 noise，h3, h4 src
    noise = add_noise(img)

    normalization = 1 # default normalization
    h1 = np.array([[1, 1, 1], 
                   [1, 1, 1],
                   [1, 1, 1]])
    h2 = np.array([[1, 2, 1],
                   [2, 4, 2],
                   [1, 2, 1]])

    if choice == 'h1':
        choice, normalization = h1, 9
        img = noise
    elif choice == 'h2':
        choice, normalization = h2, 16
        img = noise
    elif choice == 'h3':
        lap_manual(img, 'h3')
        return None
    elif choice == 'h4':
        lap_manual(img, 'h4')
        return None
    else:
        return None

    pad = np.pad(img, (1,1), mode='constant', constant_values=0)
    r, c = pad.shape
    out = np.copy(pad)
    for i in range(1, r-1):
        for j in range(1, c-1):
            res = np.sum(choice * pad[i-1:i+2, j-1:j+2])
            out[i, j] = res / normalization
    out = out[1:r-1, 1:c-1]
    cv.imwrite('output.jpg', out)
    
def main():
    choose_h(ifd1, 'h3')

if __name__ == "__main__":
    main()
