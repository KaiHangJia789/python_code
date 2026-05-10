"""
cv2.Scharr(src,ddepth,dx,dy,scale,delta,borderType)
它的卷积核默认为3*3
"""

import cv2
import numpy as np

img = cv2.imread('data/sobel.png')
# 灰度图
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Scharr算子x轴方向
x = cv2.Scharr(img,cv2.CV_64F,1,0)
#Scharr算子y轴方向
y = cv2.Scharr(img,cv2.CV_64F,0,1)

#dst = x+y
dst = cv2.add(x,y)

cv2.imshow('img',img)
cv2.imshow('x',x)
cv2.imshow('y',y)
cv2.imshow('dst',dst)
cv2.waitKey(0)