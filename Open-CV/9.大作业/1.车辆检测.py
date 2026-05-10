from math import e

import cv2
import numpy as np
#(672, 1360)
# 配置参数
min_w = 90
min_h = 90
line_higt = 500  # 检测线高度
offset = 7       # 偏移量
carno = 0        # 车辆计数
cars = []        # 存储车辆中心点

cap = cv2.VideoCapture('data/car1.mp4')
def center(x,y,w,h):
    return int(x+w/2),int(y+h/2)

# 背景减除器
bgsubmog = cv2.createBackgroundSubtractorMOG2()
#形态学kernel
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))

while True:
    ret,frame = cap.read()
    
    if ret == True:
        #灰度化
        frame_1 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        
        #去噪(高斯)
        frame_1 = cv2.GaussianBlur(frame_1,(5,5),0)
        mask = bgsubmog.apply(frame_1)#背景减除
        #腐蚀
        erode = cv2.erode(mask,kernel,iterations=1)
        
        #膨胀
        dilate = cv2.dilate(erode,kernel,iterations=3)
        #闭操作
        close = cv2.morphologyEx(dilate,cv2.MORPH_CLOSE,kernel)
        
        
        #提取车辆外形轮廓
        cnts,h= cv2.findContours(close,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        
        #画检测线线
        cv2.line(frame,(10,line_higt),(1300,line_higt),(0,255,255),3)

        for (i,c) in enumerate(cnts):
            x,y,w,h = cv2.boundingRect(c)

            #对车辆的宽高进行判断，宽高都大于阈值则认为为车辆
            isValid = (w > min_w) and (h > min_h)
            if not isValid:
                continue
            
            #到这里就可以认为该区域为车辆
            #画矩形
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

            cpoint = center(x,y,w,h)
            cars.append(cpoint)

            for (x,y) in cars:
                if((y>line_higt-offset) and(y<line_higt+offset)):
                    carno += 1
                    cars.remove((x,y))
                    print('car no:',carno)

        cv2.putText(frame,"Care Count:"+str(carno),(500,50),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,2,(0,255,255),2)
        cv2.imshow('video',frame)
        #cv2.imshow('car',close)

    key = cv2.waitKey(5)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()