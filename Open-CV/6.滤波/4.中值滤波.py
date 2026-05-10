"""
中值滤波专门用作处理胡椒噪音
cv2.medianBlur(src, ksize)
src:输入图像
ksize:核大小，必须是奇数(如3,5,7...)
"""

import cv2
import numpy as np

img= cv2.imread("data/hujiao_test.png")

dst = cv2.medianBlur(img,5)

cv2.imshow('img',img)
cv2.imshow('dst',dst)
cv2.waitKey(0)