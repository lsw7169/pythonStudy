# -*- coding: utf-8 -*-
"""
Created on Sun Jul 02 23:03:42 2017

@author: lsw71
"""

import numpy as np
import cv2

# load an color image in grayscale
img = cv2.imread('Kaleidoscope.jpg',0)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27: # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('KaleidoscopeGray.png',img)
    cv2.destroyAllWindows()
