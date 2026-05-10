import cv2
import numpy as np

img = cv2.imread('data/big_bear.png')

kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
dst = cv2.erode(img,kernel,iterations = 1)

#dst = cv2.dilate(img,kernel,iterations = 1)

cv2.imshow('img',img)
cv2.imshow('dst',dst)
cv2.waitKey(0)