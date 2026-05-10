import cv2
import numpy as np

img = np.zeros((480,640,3),np.uint8)
#参一数：图片，中心点，半径，颜色，线宽
img = cv2.rectangle(img,(100,100),(300,300),(255,255,255),5)
cv2.imshow('rectangle',img)
cv2.waitKey(0)
cv2.destroyAllWindows()