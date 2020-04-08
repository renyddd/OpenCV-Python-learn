import numpy as np
import cv2 as cv
# Create a black image
img = np.zeros((512,512,3), np.uint8)
# cv.line(img,(0,0),(511,511),(255,0,0),5)
# Draw a diagonal blue line with thickness of 5 px
cv.rectangle(img,(384,0),(510,128),(0,255,0),3)
cv.circle(img,(447,63), 63, (0,0,255), -1)
cv.imwrite('output.jpg', img)
