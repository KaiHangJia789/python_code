import cv2
import numpy as np

img = np.zeros((480,640,3),np.uint8)

cv2.putText(
    img,
    'Hello',
    (100,200),                #坐标
    cv2.FONT_HERSHEY_SIMPLEX, #字体
    3,                        #字体大小
    (255,0,0),                #颜色
    5                         #线宽
    )

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()