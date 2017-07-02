# -*- coding: utf-8 -*-
"""
Created on Sun Jul 02 23:18:16 2017

@author: lsw71
"""

import numpy as np
import cv2

#filename = 'checkerboard.png'
img = cv2.imread('Kaleidoscope.jpg')
#cv2.imshow('image',img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)

# result is dilated for marking the corners, not important
dst = cv2.dilate(dst, None)

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()] = [0,0,255]
cv2.imshow('dst',img)
cv2.waitKey(0)
if cv2.waitkey(0) & 0xff == 27:
    cv2.destroyAllWindows()
    
