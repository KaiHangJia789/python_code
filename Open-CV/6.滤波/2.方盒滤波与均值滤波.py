"""
方盒滤波:   保留亮度（不归一化）或特殊求和场景时使用
    cv2.boxFilter(src, ddepth, ksize, anchor, normalize, borderType)
    ksize	        卷积核大小
    normalize	    是否归一化
        True(=cv2.blur()):     对结果除以核的面积（均值滤波效果）
        False:      只做求和，不归一化（容易溢出）

均值滤波:   做均值模糊、降噪
    cv2.blur(src, ksize, anchor, borderType)
"""
import cv2
import numpy as np

img = cv2.imread('data/bear.png')
dst = cv2.blur(img,(5,5))

cv2.imshow('img',img)
cv2.imshow('dst',dst)
cv2.waitKey(0)