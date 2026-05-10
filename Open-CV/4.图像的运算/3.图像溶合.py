import cv2
import numpy as np

bear = cv2.imread('data/bear.png')
bear_s = cv2.imread('data/bear_s_test.png')

print(bear.shape)
print(bear_s.shape)

# 图像融合
#参数： 图像1，权重1，图像2，权重2，加权值
result = cv2.addWeighted(bear,0.3,bear_s,0.7,0) 

cv2.imshow('result',result)
cv2.waitKey(0)