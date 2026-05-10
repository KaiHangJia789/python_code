import numpy as np
import cv2

#通过array()函数创建数组
a = np.array([1,2,3])# 创建一个数组
b = np.array([[1,2,3],[4,5,6]])

# print(a)
# print(b)

#定义zeros矩阵
# 创建4个6行3列的矩阵，元素全为0
c = np.zeros((4,6,3),np.uint8)
# 创建6行3列的矩阵，元素全为0
d = np.zeros((6,3),np.uint8)
# print(c)
# print(d)

#定义ones矩阵
#创建4个6行3列的矩阵，元素全为1
e = np.ones((4,6,3),np.uint8)
#print(e)

#定义full矩阵
#创建6行3列的矩阵，元素全为5
f = np.full((6,3),5,np.uint8)
#print(f)

#定义identity矩阵 对角矩阵
#创建4行4列的矩阵，元素全为0，对角线上的元素为1
g = np.identity(4)
#print(g)

#定义eye矩阵
#创建4行5列的矩阵，元素全为0，对角线上的元素为1,K值表示对角线偏移量
h = np.eye(4,5,k = 3)
# print(h)

#===============================================================================
