import cv2
import numpy as np

# 打开视频,如果cv2.VideoCapture(0)为0则打开摄像头,为视频文件则打开视频
#若打开摄像头，最后要释放摄像头
#vc.release()
vc = cv2.VideoCapture(r'D:\python进阶\data\视频yej.mp4')

# 判断是否打开成功
if vc.isOpened():
    rval, frame = vc.read()#读取第一帧
else:
    rval = False

while rval:  # 循环读取视频帧
    ret ,frame = vc.read()
    if frame is None:
        print('视频已结束！')
        break
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#转为灰度图
        cv2.imshow('video', gray)
        if cv2.waitKey(10) & 0xFF == 27:
            break

cv2.destroyAllWindows()#销毁所有窗口 