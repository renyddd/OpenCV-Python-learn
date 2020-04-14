## OpenCV-Python
- [Official tutorial.](https://docs.opencv.org/master/d0/de3/tutorial_py_intro.html)
- [中文教程](https://www.kancloud.cn/aollo/aolloopencv/269602)
- [numpy 中文教程](https://www.numpy.org.cn/user/)
- [Pillow 中文教程](https://pillow-cn.readthedocs.io/zh_CN/latest/handbook/tutorial.html)

### GUI Features
#### Start with Images
```python
import numpy as np
import cv2 as cv
retval = cv.imread( filename[, flags] )
```
Note:
- 1: Loads a color image. The default flag.
- 0: Loads image in grayscale mode.
- -1: UNCHANGED.
Even if the image path is wrong, it won't throw any error, but print img will give you None.

#### Drawing Functions
**Drawing line**, to create a blak image and draw a blue line on it from top-left to bottom-right corners.
```python
import numpy as np
import cv2 as cv

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw diagonal blue line with thickness of 5 px
cv.line(img, (0,0), (511,511), (255,0,0), 5)
```

**Drawing rectangle**, to draw a green rectangle at the top-right corner fo image
```python
cv.rectangle(img, (384,0), (510,128), (0,255,0), 3)
```

**Drawing circle**, to draw a circle inside the rectangle drawn above with its center coordinates and radius
```python
cv.circle(img, (477,63), 63, (0,0,255), -1) # '-1' fills in the circle
```

### Core Operations
#### Basic Operations on Images
Almost all the operations in this section are mainly related to Numpy rather than OpenCV.
**Accessing and Modifying pixel values**, load a color image first:
```python
import numpy as np
import cv2 as cv
img = cv.imread('input.jpg')
```
You can access a pixel value by its row and column coordinates. For BGR image, if returns an array fo Bule, Green, Red values. For grayscale image, just corresponding intensity is returned.
```
>>> px = img[100, 100]
>>> print(px)
[VALUE, VALUE, VALUE]

# modify the pixel values the same way
img[100, 100] = [255,255,255]
```
#### Arithmetic Operations on Images
[Official.](https://docs.opencv.org/master/d0/d86/tutorial_py_image_arithmetics.html)

## NumPy
[Official Tutorials](https://numpy.org/devdocs/user/tutorials_index.html)
### Basics
**Array creation**, convert python array-like objects to numpy arrays, for examples lists and tuples. Built-in functions for creation, **zeros(shape), ones(type), arange()** will create an array filled with 0, 1, regularly incrementing values.
```python
x = np.array([3, 2, 5, 8, 4, 7])
```
**Element indexing**, 0-based and accept negative indices.
```python
x = np.arange(10)
print(x[2])
x.shape = (2,5) # 2-dimensional
print(x[1,-1])
```

## Pillow
get the image, gray, then use cv write down.
```python
import cv2 as cv    
import numpy as np    
from PIL import Image    

ifd = 'input.jpg'    
ofd = 'output.jpg'    

img = Image.open(ifd)    
grey_img = np.array(img.convert('L'))    

print(grey_img)    
```
