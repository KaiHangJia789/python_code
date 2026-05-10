"""
cv2.morphologyEx(图片, 操作类型, 核)
    专门用来给黑白二值图做：去噪点、补洞、修形状、粗细调整。

最常用的 4 种操作类型（背这 4 个就够）
1. cv2.MORPH_OPEN 开运算
    作用：去掉小白点噪点
2. cv2.MORPH_CLOSE 闭运算
    作用：补上小黑洞
3. cv2.MORPH_GRADIENT 梯度
    作用：提取物体轮廓、边缘
4. cv2.MORPH_TOPHAT / MORPH_BLACKHAT
    用来增强亮区 / 暗区
"""

import cv2
import numpy as np

img = cv2.imread('data/morph_close.jpg')

kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(17,17))

dst = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)

cv2.imshow('img',img)
cv2.imshow('dst',dst)
cv2.waitKey(0)
