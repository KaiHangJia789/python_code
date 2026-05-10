"""处理高通滤波
索贝尔算法: 专门用来检测图像的水平 / 垂直边缘
cv2.Sobel(
    src,        # 输入图像
    ddepth,     # 输出图像深度（必须指定！）
    dx,         # x 方向导数阶数
    dy,         # y 方向导数阶数
    ksize,      # 卷积核大小  |设置为-1,自动变成沙尔算法
    scale,      # 缩放因子（可选）
    delta,      # 偏移量（可选）
    borderType  # 边界填充方式（可选）
)
"""
import cv2
import numpy as np

img = cv2.imread('data/sobel.png')
# 灰度图
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#索贝尔算子x轴方向
x = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
#索贝尔算子y轴方向
y = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)

#dst = x+y
dst = cv2.add(x,y)

cv2.imshow('img',img)
cv2.imshow('x',x)
cv2.imshow('y',y)
cv2.imshow('dst',dst)
cv2.waitKey(0)