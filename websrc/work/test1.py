import cv2
import numpy as np

# 读取一张斯里兰卡拍摄的大象照片
img = cv2.imread('input.jpg')

# 沿着横纵轴放大1.6倍，然后平移(-150,-240)，最后沿原图大小截取，等效于裁剪并放大
M_crop_elephant = np.array([
    [1.6, 0, -150],
    [0, 1.6, -240]
    ], dtype=np.float32)

img_elephant = cv2.warpAffine(img, M_crop_elephant, (400, 600))
cv2.imwrite('output.jpg', img_elephant)
