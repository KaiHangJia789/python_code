import cv2
import numpy as np

def cv2_show(name,img):
    if img is not None:
        cv2.imshow(name, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print('图片不存在！')

path = 'D:\python进阶\data\picture_str(count).png'
img = cv2.imdecode(np.fromfile(path, dtype=np.uint8), cv2.IMREAD_COLOR)
#cv2_show('picture',img)

#截取图片
# part = img[0:100,0:100]
# cv2_show('part',part)

#_________________________________________________________
#颜色通道获取
b,g,r = cv2.split(img)
# cv2_show('b',b)

#cv2.merge([b,g,r]):合并
img = cv2.merge([b,g,r])

#只保留R
cur_img = img.copy()
cur_img[:,:,0] = 0
cur_img[:,:,1] = 0
cv2_show('R',cur_img)

#只保留G
cur_img = img.copy()
cur_img[:,:,0] = 0
cur_img[:,:,2] = 0
cv2_show('G',cur_img)