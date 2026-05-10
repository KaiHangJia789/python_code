import cv2

fourcc = cv2.VideoWriter_fourcc(*'mp4v')#视频编码格式
vw = cv2.VideoWriter('./out.mp4', fourcc, 20.0, (640, 480))#输出视频文件名，编码格式，帧率，分辨率

#创建窗口
cv2.namedWindow("video", cv2.WINDOW_NORMAL)#windows_normal可以调整窗口大小  
cv2.resizeWindow("video", 640, 480)#调整窗口大小为640x480

#获取视频设备
cap = cv2.VideoCapture(0)#0为摄像头

while cap.isOpened():#如果视频设备打开成功
    #获取视频帧
    ret,frame = cap.read()#ret为是否成功获取帧，frame为获取的帧
    if ret:
        cv2.imshow("video", frame)#显示视频帧
        #重新调整窗口大小为640x480
        cv2.resizeWindow("video", 640, 480)
        vw.write(frame)#写入视频帧
        
        key = cv2.waitKey(50)#1ms
        if (key & 0xFF == ord('q')):#按q退出
            break
    else:
        break

#释放视频设备
cap.release()
vw.release()
cv2.destroyAllWindows()