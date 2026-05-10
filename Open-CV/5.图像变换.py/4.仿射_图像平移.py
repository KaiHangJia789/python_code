"""
仿射:平移、旋转、缩放、倾斜的结合
warpAffine(src, M, dsize,flags,mode,value)
M: 变换矩阵
dsize: 输出图像大小
flags: 插值方法与resize方法一样
mode: 边界模式
value: 边界值

平移矩阵:
矩阵中的每个像素由(x,y)组成
因此:其变换矩阵是2*2的矩阵
平移向量为2*1的向量,所在的平移矩阵为2*3的矩阵

"""

import cv2
import numpy as np

big_bear = cv2.imread('data/big_bear.png')
y,x,ch= big_bear.shape
# 平移向量
M = np.float32([[1,0,100],[0,1,50]])
new = cv2.warpAffine(big_bear,M,(x,y))

cv2.imshow('big_bear',big_bear)
cv2.imshow('new',new)
cv2.waitKey(0)