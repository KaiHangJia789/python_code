"""
resize(img, (width, height), interpolation=INTER_LINEAR)
插值方式	    英文全称		速度
INTER_NEAREST	最近邻插值		最快
INTER_LINEAR	双线性插值		快
INTER_AREA	    区域插值		中等
INTER_CUBIC	    双三次插值	    最慢
"""

import cv2
import numpy as np

big_bear = cv2.imread('data/big_bear.png')
#new = cv2.resize(big_bear,(400,400))
#参数:图片，赋值变量，缩放比例，插值方法
#插值方法分为四种，INTER_NEAREST,INTER_LINEAR,INTER_AREA,INTER_CUBIC
new = cv2.resize(big_bear,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)

cv2.imshow('big_bear',big_bear)
cv2.imshow('new',new)
cv2.waitKey(0)