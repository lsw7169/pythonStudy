# -*- coding: utf-8 -*-
"""
Created on Mon Jul 03 00:36:02 2017

@author: lsw71
"""

import numpy as np
import cv2 as cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('Kaleidoscope.jpg')
img2 = cv2.imread('patch.jpg')

# Initiate SIFT detector
orb = cv2.ORB_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

# create BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

# Match descriptors.
matches = bf.match(des1,des2)

# Sort them in the order of their distance.
matches = sorted(matches, key=lambda x:x.distance)

# Convert BGR 2 RGB
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

# Draw first 10 matches
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:100],None, flags=2)

plt.imshow(img3),plt.show()