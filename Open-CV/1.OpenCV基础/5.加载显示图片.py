#"D:\huiyeji.png"

import cv2

cv2.namedWindow("Image", cv2.WINDOW_NORMAL)#windows_normal可以调整窗口大小

img = cv2.imread("D:\\huiyeji.png")#读取图像

cv2.imshow('img', img)#显示图像
while True:
    key = cv2.waitKey(0)
    if (key & 0xFF == ord('q')):#按q退出
        
        break
cv2.destroyAllWindows()#销毁所有窗口