import cv2
import numpy as np

def callback():
    pass
cv2.namedWindow('Trackbar', cv2.WINDOW_NORMAL)

# 创建3个滑动条trackbar，分别控制R、G、B的值，范围为0-255，回调函数为callback
cv2.createTrackbar('R', 'Trackbar', 0, 255, callback)
cv2.createTrackbar('G', 'Trackbar', 0, 255, callback)
cv2.createTrackbar('B', 'Trackbar', 0, 255, callback)

img = np.zeros((480, 640, 3), dtype=np.uint8)  # 创建一个全零的图像

while True:
    r = cv2.getTrackbarPos('R', 'Trackbar')  # 获取R滑动条的值
    g = cv2.getTrackbarPos('G', 'Trackbar')  # 获取G滑动条的值
    b = cv2.getTrackbarPos('B', 'Trackbar')  # 获取B滑动条的值
    img[:] = [b, g, r]  # 根据滑动条的值更新图像颜色

    cv2.imshow('Trackbar', img)  # 显示图像
    
    key = cv2.waitKey(10) 

    if (key & 0xFF == ord('q')):  # 按q退出
        break

cv2.destroyAllWindows()