"""
把灰度图变成【黑白对比强烈】的二值图，
专门解决：光照不均、有阴影、光线暗的图片。
"""

import cv2
import numpy as np

img = cv2.imread('data/adaptiveshresh.png')
img_1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

dst = cv2.adaptiveThreshold(
                    img_1,#灰度图
                    255,    #阈值
                    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,#计算阈值方式
                    cv2.THRESH_BINARY_INV, #二值化
                    11, #邻域块大小 = 11×11
                    0)  #微调值 C = 0
print(dst.shape)

cv2.imshow('img',img)
cv2.imshow('img_1',img_1)
cv2.imshow('dst',dst)

cv2.waitKey(0)