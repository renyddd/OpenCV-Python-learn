## OpenCV-Python
[Official tutorial.](https://docs.opencv.org/master/d0/de3/tutorial_py_intro.html)

### Start with Images
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
