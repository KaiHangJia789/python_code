import cv2
import numpy as np
#鼠标回调函数
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:#左键按下
        print("Left button down at ({}, {})".format(x, y))
    elif event == cv2.EVENT_LBUTTONUP:#左键抬起
        print("Left button up at ({}, {})".format(x, y))
    elif event == cv2.EVENT_RBUTTONDOWN:#右键按下
        print("Right button down at ({}, {})".format(x, y))
    elif event == cv2.EVENT_RBUTTONUP:#右键抬起
        print("Right button up at ({}, {})".format(x, y))
    elif event == cv2.EVENT_MOUSEMOVE:#鼠标移动
        print("Mouse move at ({}, {})".format(x, y))

#创建窗口
cv2.namedWindow('video',cv2.WINDOW_NORMAL)
cv2.resizeWindow('video',640,480)

#设置鼠标回调
#参数1：窗口名,参数2：回调函数,参数3：回调函数的参数
cv2.setMouseCallback('video',mouse_callback,"001")

img = np.zeros((480,640,3),dtype=np.uint8)#创建一个全零的图像
while True:
    #显示图像
    cv2.imshow('video',img)
    #等待按键
    key = cv2.waitKey(1)
    if (key & 0xFF == ord('q')):#按q退出
        break
  
cv2.destroyAllWindows()
 
