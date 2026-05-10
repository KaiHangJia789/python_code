import cv2
import numpy as np

bear = cv2.imread('data/bear.png')
bear_s = cv2.imread('data/bear_s_test.png')
#print(bear.shape)  (293,245,3)
print(bear_s.shape)

#创建一个全为1的矩阵
#img = np.ones((293,245,3),np.uint8) * 100

cv2.imshow('img',bear)

result = cv2.add(bear,bear_s)

cv2.imshow('result',result)
cv2.waitKey(0)