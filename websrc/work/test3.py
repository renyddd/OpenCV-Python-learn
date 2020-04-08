import cv2
import numpy as np

rgb_img = cv2.imread('input.jpg')
gray_img = cv2.cvtColor(rgb_img, cv2.COLOR_BGR2GRAY)
reverse_img = 255 - gray_img

cv2.imwrite('output.jpg', reverse_img)
