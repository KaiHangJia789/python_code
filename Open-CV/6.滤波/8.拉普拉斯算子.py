"""
cv2.LaPlacian(src, ddepth, ksize=None,
             scale=1, delta=0, borderType=None)
"""

import cv2
import numpy as np

img = cv2.imread('data/sobel.png')
# 灰度图
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

x = cv2.Laplacian(img,cv2.CV_64F,ksize=3)

cv2.imshow('img',img)
cv2.imshow('x',x)

cv2.waitKey(0)