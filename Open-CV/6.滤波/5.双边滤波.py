"""
cv2.bilateralFilter(src, d, sigmaColor, sigmaSpace)
src:输入图像
d:  滤波时每个像素的邻域直径
    d>0:直接指定邻域大小
    d<=0:根据sigmaSpace的值计算邻域大小

sigmaColor: 颜色空间中邻域像素的权重系数
sigmaSpace: 空间空间中邻域像素的权重系数

"""

import cv2
import numpy as np
cv2.namedWindow('img')

img = cv2.imread('data/self_img.jpg')
print(img.shape)
img_1 = cv2.resize(img,(1080,1080))
dst = cv2.bilateralFilter(img_1,9,30,75)

cv2.imshow('img',img_1)
cv2.imshow('dst',dst)
cv2.waitKey(0)
