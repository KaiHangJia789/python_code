import cv2
import numpy as np

img = cv2.imread('data/erode.jpg')

# 创建核
#kernel = cv2.getStructuringElement(核的类型，核的大小:如(5,5))
#核的类型:
    #MORPH_RECT:矩形核
    #MORPH_CROSS:十字形核
    #MORPH_ELLIPSE:椭圆核
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
print(kernel)

dst = cv2.erode(img,kernel,iterations = 1)

cv2.imshow('img',img)
cv2.imshow('dst',dst)
cv2.waitKey(0)