import cv2

cv2.namedWindow("Image", cv2.WINDOW_AUTOSIZE)#创建窗口
cv2.resizeWindow("Image", 400, 400)#调整窗口大小
cv2.imshow('Image', 0)#显示图像

key = cv2.waitKey(0)#暂停程序
if key == ord('q'):#按q退出
    exit(0)
cv2.destroyAllWindows()#销毁所有窗口