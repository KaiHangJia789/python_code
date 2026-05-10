"""
approx = cv2.approxPolyDP(多边形逼近)
(
    contours[0], 必须是单个轮廓（不能传列表)
    epsilon,     逼近精度，值越小越接近原图，值越大越简化。
    True         表示轮廓是闭合的)

hull = cv2.convexHull(凸包)
    (contours[0]    必须是单个轮廓（不能传列表)
    )
"""
import cv2
import numpy as np

def drawShape(src,points):
    i  = 0
    while i<len(points):
        if i == len(points)-1:
            x,y = points[i][0]
            x1,y1 = points[0][0]
            cv2.line(src, (x,y),(x1,y1),(0,255,0),1)
        else:
            x,y = points[i][0]
            x1,y1 = points[i+1][0]
            cv2.line(src, (x,y),(x1,y1),(0,255,0),1)
        i += 1

img = cv2.imread('data/hand.png')
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

e = 10
approx = cv2.approxPolyDP(contours[0],e,True)
drawShape(img,approx)

hull = cv2.convexHull(contours[0])
drawShape(img,hull)

cv2.imshow('img',img)
# cv2.imshow('gray',gray)
# cv2.imshow('binnary',binnary)
cv2.waitKey(0)