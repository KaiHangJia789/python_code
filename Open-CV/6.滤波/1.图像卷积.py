"""二维卷积滤波

低通滤波:可以 去除噪音 或 平滑图像
高通滤波:可以 提取图像的 边缘
cv2.filter2D(src, ddepth, kernel, anchor, delta, borderType)

src:输入图像
ddepth: 输出图像的深度
        [-1:和输入图像保持一致,cv2.CV_8U:8 位无符号整数]
kernel: 卷积核
    [一个二维 numpy 数组，比如 np.ones((3,3))/9]
anchor: 锚点
        [默认值 (-1, -1)：表示锚点在卷积核的正中心]
delta:  偏移量
        [默认值 0: 不加偏移]
borderType:边界填充模式
    [  cv2.BORDER_REFLECT:  镜像填充（效果自然，最常用）
       cv2.BORDER_CONSTANT: 用固定值填充（如黑色 / 白色）
       cv2.BORDER_REPLICATE:复制边缘像素
    ]
"""
import cv2
import numpy as np

img = cv2.imread('data/bear.png')
kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)

cv2.imshow('img',img)
cv2.imshow('dst',dst)
cv2.waitKey(0)