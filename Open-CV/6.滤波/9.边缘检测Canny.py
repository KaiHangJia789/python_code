"""
cv2.Canny(
    image,          # 输入图像（灰度图）
    threshold1,     # 低阈值
    threshold2,     # 高阈值
    apertureSize=3, # Sobel 核大小（可选）
    L2gradient=False # 梯度计算方式（可选）
"""

import cv2  
import numpy as np

img = cv2.imread('data/lena.png')

dst = cv2.Canny(img,120,250)

cv2.imshow('img',img)
cv2.imshow('dst',dst)
cv2.waitKey(0)