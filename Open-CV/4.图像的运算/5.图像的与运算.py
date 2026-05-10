"""
创建一个黑白图，通过与运算,
提取感兴趣区域（ROI）、遮挡无用区域、保留指定部分。
"""
import cv2
import numpy as np

# 创建一个黑白图片
img = np.zeros((200,200),np.uint8)
img_2 = np.zeros((200,200),np.uint8)
bear = cv2.imread('data/bear.png')
bear_s = cv2.imread('data/bear_s_test.png')

img[20:120,20:120] = 255
img_2[80:180,80:180] = 255
# 进行与运算
new_img = cv2.bitwise_and(img,img_2)
new_bear = cv2.bitwise_and(bear,bear_s)


# cv2.imshow('img',img)
# cv2.imshow('img_2',img_2)
# cv2.imshow('new_img',new_img)

cv2.imshow('bear',bear)
cv2.imshow('bear_s',bear_s)
cv2.imshow('new_bear',new_bear)

cv2.waitKey(0)