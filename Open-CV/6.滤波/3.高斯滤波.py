"""
cv2.GaussianBlur(img,kernel,sigmaX,sigmaY,borderType,...)

    kernel	高斯核大小	必须为奇数。
    sigmaX	X 轴标准差  通常设为 0 让程序自动计算。
    sigmaY	Y 轴标准差  若设为 0,则等于 sigmaX;
                        若两者均为 0,根据核大小自动计算。
                        
"""

import cv2
import numpy as np

img = cv2.imread('data/bear.png')

dst_0 = cv2.GaussianBlur(img,(5,5),0)
dst_1 = cv2.GaussianBlur(img,(5,5),4)
dst_2 = cv2.GaussianBlur(img,(5,5),10000000)

cv2.imshow('img',img)
cv2.imshow('dst_0',dst_0)
cv2.imshow('dst_1',dst_1)
cv2.imshow('dst_2',dst_2)
cv2.waitKey(0)

