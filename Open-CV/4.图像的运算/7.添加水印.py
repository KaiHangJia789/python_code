"""
1. 引入一幅图片,img
2. 要有一个LOGO，自己创建
3. 计算图片在什么地方添加，再添加的地方变成黑色
4。 利用add,将logo,与 图片叠加到一起"""

import cv2
import numpy as np

#导入图片
img = cv2.imread('data/big_bear.png')

#创建logo
logo = np.zeros((200,200,3),np.uint8)
#创建mask:掩码
mask = np.zeros((200,200),np.uint8)

#绘制logo
logo[20:120,20:120] = [150,0,0]
logo[80:180,80:180] = [0,150,0]

mask[20:120,20:120] = 255
mask[80:180,80:180] = 255

#对msak按位求反
m = cv2.bitwise_not(mask)

#选择img 添加logo的位置
roi = img[0:200,0:200]

#与m进行与运算
tmp = cv2.bitwise_and(roi,roi,mask = m)

#与logo进行与运算,深拷贝,不能加到原图片中
dst = cv2.add(tmp,logo)
#浅拷贝
img[0:200,0:200] = dst

cv2.imshow('img',img)
cv2.imshow('dst',dst)
# cv2.imshow('tmp',tmp)
# cv2.imshow('m',m)
# cv2.imshow('mask',mask)
# cv2.imshow('logo',logo)
cv2.waitKey(0)