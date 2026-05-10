"""
getRotationMatrix2D(center,angle, scale)
center:旋转中心点
angle:旋转角度
scale:缩放比例
"""
import cv2
import numpy as np

big_bear = cv2.imread('data/big_bear.png')
y,x,ch= big_bear.shape

# 旋转向量
#旋转的角度是逆时针
#M = np.float32([[1,0,100],[0,1,50]])
M = cv2.getRotationMatrix2D((x/2,y/2),45,1)
new = cv2.warpAffine(big_bear,M,(int(x/2),int(y/2)))

cv2.imshow('big_bear',big_bear)
cv2.imshow('new',new)
cv2.waitKey(0)