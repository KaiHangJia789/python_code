import cv2
import numpy as np

img = np.zeros((480,640,3),np.uint8)
#参一数：图片，中心点，半径，颜色，线宽
cv2.circle(img,(320,240),100,(0,0,255),-1)
cv2.imshow('circle',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
