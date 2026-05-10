import cv2

cv2.namedWindow("video", cv2.WINDOW_NORMAL)#windows_normal可以调整窗口大小  
cv2.resizeWindow("video", 640, 480)#调整窗口大小为640x480

#获取视频设备
cap = cv2.VideoCapture(0)#0为摄像头

while True:
    #获取视频帧
    ret,frame = cap.read()#ret为是否成功获取帧，frame为获取的帧
    cv2.imshow("video", frame)#显示视频帧

    key = cv2.waitKey(1)#1ms
    if (key & 0xFF == ord('q')):#按q退出
        break

#释放视频设备
cap.release()
cv2.destroyAllWindows()