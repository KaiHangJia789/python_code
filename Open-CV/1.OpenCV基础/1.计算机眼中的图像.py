"""
cv2.IMREAD_COLOR:彩色图像
cv2.IMREAD_GRAYSCALE:灰度图像
"""

import cv2
import numpy as np


def cv2_show(name,img):
    if img is not None:
        cv2.imshow(name, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print('图片不存在！')


# 读取图片
path = r'D:\python进阶\data\picture_str(count).png'
#解决图片中文乱码
img = cv2.imdecode(np.fromfile(path, dtype=np.uint8), cv2.IMREAD_COLOR)

# if img is None:
#     print('图片不存在！')
#     exit()
# # 显示图片
# cv2.imshow('picture', img)
# # 等待显示
# cv2.waitKey(0)
# cv2.destroyAllWindows()#销毁所有窗口

# 图片的尺寸
img_shape_color = img.shape
print(img_shape_color)

#灰度图片
img = cv2.imdecode(np.fromfile(path, dtype=np.uint8), cv2.IMREAD_GRAYSCALE)
img_shape_gary = img.shape
print(img_shape_gary)

# cv2_show('picture', img)

# #保存
# cv2.imencode("灰度辉夜姬.png",img)[1].tofile(r"D:\python进阶\data灰度辉夜姬.png")

# 图片类型
type_img = type(img)
print(type_img)

# 图片大小
size_img = img.size
print(size_img)

# 图片数据类型
dtype_img = img.dtype
print(dtype_img)