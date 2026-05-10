"""
getAffineTransform(src[], dst[])
参数: src, dst

通过三个点可以确定变换的位置
"""

import cv2
import numpy as np

big_bear = cv2.imread('data/big_bear.png')
y,x,ch= big_bear.shape

src = np.float32([[300,200],[600,300],[800,800]])
dst = np.float32([[200,300],[400,500],[600,800]])

M = cv2.getAffineTransform(src,dst)

new = cv2.warpAffine(big_bear,M,(x,y))

cv2.imshow('big_bear',big_bear)
cv2.imshow('new',new)
cv2.waitKey(0)