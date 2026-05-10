"""
warpPerspective(img,M,dsize)
M:变换矩阵
dsize:输出图像大小

getPerspectiveTransform(src, dst)
src:变换前的图像坐标点
dst:变换后的图像坐标点
    需要四个点的坐标点
"""

import cv2
import numpy as np

img = cv2.imread('data\ma_promb.png')

src = np.float32([[100,600],[1400,600],[10,2222],[1540,2222]])
dst = np.float32([[0,0],[1880,0],[0,2222],[1880,2222]])
M = cv2.getPerspectiveTransform(src,dst)

new = cv2.warpPerspective(img,M,(1880,2222))
cv2.imshow('img',img)
cv2.imshow('new',new)
cv2.waitKey(0)
