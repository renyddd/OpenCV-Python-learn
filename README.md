## OpenCV-Python
[Official tutorial.](https://docs.opencv.org/master/d0/de3/tutorial_py_intro.html)

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
cv.circle(img, (477,63), 63, (0,0,255), -1)
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
