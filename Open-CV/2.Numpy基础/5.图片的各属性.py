import cv2
import numpy as np

img = cv2.imread(r'data\huiyeji.png')

# 获取图片的宽高和通道数
print(img.shape)

# 获取图片的大小:宽*高*通道数
print(img.size)

# 获取图片的数据类型,每个元素的位深
print(img.dtype)