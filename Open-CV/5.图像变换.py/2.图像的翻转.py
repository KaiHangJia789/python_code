"""
flip(img,flipCode)
flipCode==0:上下翻转
flipCode >1:左右翻转
flipCode <0:左右 + 上下翻转
"""

import cv2
import numpy as np

big_bear = cv2.imread('data/bear.png')
new_0 = cv2.flip(big_bear,0)
new_1 = cv2.flip(big_bear,1)
new_2 = cv2.flip(big_bear,-1)

cv2.imshow('big_bear',big_bear)
cv2.imshow('new_0',new_0)
cv2.imshow('new_1',new_1)
cv2.imshow('new_2',new_2)
cv2.waitKey(0)
