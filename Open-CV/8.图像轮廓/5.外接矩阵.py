"""
minAreaRect = 斜的、最小面积、旋转矩形
boundingRect = 正的、轴对齐、快速矩形
    minAreaRect(contour)
        输入：单个轮廓
        返回：(中心坐标(x,y), (宽w,高h), 旋转角度)
    boxPoints(r)
        把上面的返回值，转成矩形的 4 个顶点坐标
    drawContours(img,[box], ...)
        画出这个斜矩形
"""
import cv2
import numpy as np
img = cv2.imread('data/Hello.png')
print(img.shape)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(gray.shape)

# 二值化
ret,binnary = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
print(binnary.shape)

# 查找轮廓
contours,hierarchy = cv2.findContours(
    binnary,
    cv2.RETR_TREE,
    cv2.CHAIN_APPROX_SIMPLE
    )
print(contours)

# 绘制轮廓
cv2.drawContours(img,contours,0,(0,255,0),1)

# 最小外接矩形
r = cv2.minAreaRect(contours[1])
box = cv2.boxPoints(r)#获取最小外接矩形的4个顶点
box = np.intp(box)      #转换成整数型
cv2.drawContours(img,[box],0,(0,0,255),1)

x,y,w,h = cv2.boundingRect(contours[1])#获取最小外接矩形的坐标和宽高
cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),1)#绘制矩形

cv2.imshow('img',img)
cv2.waitKey(0)