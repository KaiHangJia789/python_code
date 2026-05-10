import cv2
import numpy as np

img = cv2.imread('data/erode.jpg')

# 创建卷积核
kernel = np.ones((5,5),np.uint8)
# 腐蚀
# 参数：图片，核，腐蚀次数
dst = cv2.erode(img,kernel,iterations = 2)

cv2.imshow('img',img)
cv2.imshow('dst',dst)
cv2.waitKey(0)