"""
cv2.drawContours(
    image,          #画图的原图
    contours,       #cv2.findContours 得到的轮廓列表
    contourIdx,     #-1表示绘制所有轮廓 数字 (0,1,2...)：只画第 N 个单独轮廓
    color,          #颜色    BGR格式
    thickness=None,#线宽
    ...)
"""

import cv2
import numpy as np

img = cv2.imread('data/bear.png')
print(img.shape)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(gray.shape)

# 二值化
ret,binnary = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
print(binnary.shape)

# 查找轮廓
contours,hierarchy = cv2.findContours(binnary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(contours)

# 绘制轮廓
cv2.drawContours(img,contours,-1,(0,255,0),1)

cv2.imshow('img',img)
# cv2.imshow('gray',gray)
# cv2.imshow('binnary',binnary)
cv2.waitKey(0)