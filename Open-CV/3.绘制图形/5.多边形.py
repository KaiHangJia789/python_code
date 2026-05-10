import cv2
import numpy as np

img = np.zeros((480,640,3),np.uint8)
#多边形
#参数：图片，顶点坐标，是否闭合，颜色，线宽

#顶点坐标
pts = np.array(
    [[100,100],[200,100],[300,200],[200,300],[100,200]],
    np.int32
    )
#转换为多维数组
#(-1:自动计算点数,固定维度,坐标维度(2:x,y))
pts = pts.reshape((-1,1,2))
#画线
#参数：图片，顶点坐标，是否闭合，颜色，线宽
cv2.polylines(img,[pts],True,(255,0,0),5)
#填充
#参数：图片，顶点坐标，颜色
cv2.fillPoly(img,[pts],(0,255,0))


cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
