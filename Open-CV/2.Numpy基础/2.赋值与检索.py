import numpy as np
import cv2


                            #检索与赋值

img = np.zeros((400,600,3),np.uint8)

print(img[100,100])

count = 0
while count < 200:
    #参一: 行, 参二: 列, 参三: 颜色 BGR
    img[count,count,0] = 255
    count += 1


cv2.imshow('img',img)#显示图片
key = cv2.waitKey(0)
if key == ord('q'):
    cv2.destroyAllWindows()
