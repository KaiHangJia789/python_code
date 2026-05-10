import cv2
import numpy as np

img = np.zeros((600, 400, 3), np.uint8)

#创建一个全零的图像
#split()函数: 将图像进行分离,深拷贝
b,g,r = cv2.split(img)

b[10:100, 10:100] = 255
g[10:100, 10:100] = 255

#merge()函数: 合并,深拷贝
img2 = cv2.merge([b,g,r]) 

cv2.imshow('img',img)
cv2.imshow('b',b)
cv2.imshow('g',g)
cv2.imshow('img2',img2)

cv2.waitKey(0)