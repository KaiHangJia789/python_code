import cv2
import numpy as np

img = np.zeros((480,640,3),np.uint8)
#参数:图片 (中心点坐标) (长轴和短轴长度) 旋转角度 起始角度 
# 结束角度 (颜色) 线宽(-1:填充)
#椭圆
cv2.ellipse(img,(320,240),(100,50),90,0,360,(0,255,0),1)

cv2.imshow('ellipse',img)
cv2.waitKey(0)
cv2.destroyAllWindows()