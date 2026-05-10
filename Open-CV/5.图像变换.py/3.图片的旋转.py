""" 
rotate(img,rotateCode)
ROTATE_90_CLOCKWISE :       顺时针旋转90度
ROTATE_90_COUNTERCLOCKWISE : 逆时针旋转90度
ROTATE_180 :                旋转180度
"""

import cv2
import numpy as np

big_bear = cv2.imread('data/big_bear.png')
new_1 = cv2.rotate(big_bear,cv2.ROTATE_90_CLOCKWISE)
new_2 = cv2.rotate(big_bear,cv2.ROTATE_90_COUNTERCLOCKWISE)
new_3 = cv2.rotate(big_bear,cv2.ROTATE_180)

cv2.imshow('new_180',new_3)
cv2.imshow('new_90',new_2)
cv2.imshow('big_bear',big_bear)
cv2.imshow('new_90',new_1)
cv2.waitKey(0)