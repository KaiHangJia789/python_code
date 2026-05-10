"""
area = cv2.contourArea(contour[1]):计算一个轮廓的面积
只有 1 个必选参数：
contours[1]：单个轮廓
注意：必须是某一个轮廓，不能是整个轮廓列表！

perimeter = cv2.arcLength(contour[1],True):计算一个轮廓的周长
第 1 个参数:contours[1] → 单个轮廓
第 2 个参数:True / False
True:   轮廓是闭合的（会自动把首尾连起来算周长）
False:  轮廓是开放的（只算线段长度）
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
cv2.drawContours(img,contours,1,(0,255,0),1)

#计算面积
area = cv2.contourArea(contours[1])
print("area= %d"%(area))

#计算周长
len = cv2.arcLength(contours[1],True)
print("len= %d"%(len))

cv2.imshow('img',img)
# cv2.imshow('gray',gray)
# cv2.imshow('binnary',binnary)
cv2.waitKey(0)