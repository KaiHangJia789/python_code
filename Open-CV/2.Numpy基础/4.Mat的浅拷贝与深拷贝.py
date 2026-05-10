import cv2
import numpy as np

# 读取图片
img = cv2.imread('data/bear.png')

# 浅拷贝
img_2 = img

#深拷贝
img_3 = img.copy()

img[10:100,10:100] = [0,0,255]

cv2.imshow('img',img)
cv2.imshow('img_2',img_2)
cv2.imshow('img_3',img_3)
cv2.waitKey(0)