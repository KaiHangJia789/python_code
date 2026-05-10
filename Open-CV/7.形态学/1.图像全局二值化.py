import cv2
import numpy as np

img = cv2.imread('data/big_bear.png')
# 灰度化
img_1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

"""
阈值,转化后的二值图 = cv2.threshold(原图, 阈值, 最大值, 类型)
    类型:
        1.THRESH_BINARY → 大于阈值变白，否则变黑（你现在用的）
        2.THRESH_BINARY_INV → 反色（大于阈值变黑，否则变白）
        3.THRESH_TRUNC → 大于阈值就截断成阈值
        4.THRESH_TOZERO → 小于阈值变 0
"""
ret,dst= cv2.threshold(img_1,60,255,cv2.THRESH_BINARY_INV)
print(dst.shape)

cv2.imshow('img',img)
cv2.imshow('img_1',img_1)
cv2.imshow('dst',dst)

cv2.waitKey(0)