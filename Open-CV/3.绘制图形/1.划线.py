import cv2
import numpy as np

img = np.zeros((480,640,3),np.uint8)
#参一数：图片，起始点， 结束点，   颜色， 线宽
#划线,坐标点为(x,y)
cv2.line(img,(10,20),(300,400),(0,0,255),15)
cv2.line(img,(15,25),(350,450),(0,0,255),5)

cv2.imshow('line',img)
cv2.waitKey(0)