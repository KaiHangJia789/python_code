"""
contours, hierarchy = cv2.findContours(
    binary,        # 二值化图像（必须！）
    cv2.RETR_TREE, # 轮廓检索模式
    cv2.CHAIN_APPROX_SIMPLE  # 轮廓近似方法
)

 两个返回值
① contours(轮廓):是一个列表,里面装着所有物体的轮廓点

② hierarchy(层级):是一个列表，里面装着所有轮廓的层级
轮廓检索模式：
    1. cv2.RETR_EXTERNAL 只返回最外层轮廓
    2. cv2.RETR_LIST 返回所有轮廓
    3. cv2.RETR_TREE 返回所有轮廓，并生成层级关系
    4. cv2.RETR_CCOMP 返回所有轮廓，并生成两层关系

轮廓点压缩方式:
    1. cv2.CHAIN_APPROX_NONE 存储所有的轮廓点
    2. cv2.CHAIN_APPROX_SIMPLE 压缩水平、垂直和斜线
"""
import cv2
import numpy as np

img = cv2.imread('data/bear.png')
print(img.shape)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(gray.shape)

# 二值化
ret,binnary = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
print(binnary.shape)

# 查找轮廓
contours,hierarchy = cv2.findContours(binnary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(contours)

cv2.imshow('img',img)
cv2.imshow('gray',gray)
cv2.imshow('binnary',binnary)
cv2.waitKey(0)