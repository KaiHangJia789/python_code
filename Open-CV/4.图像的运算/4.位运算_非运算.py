"""
创建一个黑白图，通过非运算，进行黑白颠倒"""

import cv2
import numpy as np

# 创建一个黑白图片
img = np.zeros((200,200),np.uint8)

bear = cv2.imread('data/bear.png')
img[50:150,50:150] = 255

# 进行非运算
new_img = cv2.bitwise_not(img)
new_bear = cv2.bitwise_not(bear)

cv2.imshow('img',img)
cv2.imshow('new_img',new_img)
cv2.imshow('bear',new_bear)
cv2.waitKey(0)