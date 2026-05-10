import cv2
import numpy as np
"""
基本功能:
    按 l 键画线
    按 r 键画矩形
    按 c 键画圆
    鼠标拖动即可绘制图形
"""

#显示窗口和背景
img = np.zeros((480,640,3),dtype=np.uint8)#创建一个全零的图像

currentshape = 0
startpos = (0,0)
#备份原始画布,实现实时绘制时刷新背景
img_backup = img.copy()
#标记鼠标是否按下
is_mouse_down = False
def mouse_callback(event, x, y, flags, param):
    #print(event, x, y, flags, param)
    global startpos,currentshape,is_mouse_down,img_backup,img
    
    if (event & cv2.EVENT_LBUTTONDOWN == cv2.EVENT_LBUTTONDOWN):
            startpos = (x,y)
            is_mouse_down = True

    elif event == cv2.EVENT_MOUSEMOVE:
        if is_mouse_down:
             #每次都从备份画布刷新,清除上一帧的预览
            img = img_backup.copy()


            if currentshape == 0:#画线
                cv2.line(img,startpos,(x,y),(255,0,0),1)
            elif currentshape == 1:#画矩形
                cv2.rectangle(img,startpos,(x,y),(0,255,0),1)
            elif currentshape == 2:#画圆
                a = (x - startpos[0])
                b = (y - startpos[1])
                r = int((a*a + b*b)**0.5)
                cv2.circle(img,startpos,r,(0,0,255),1)
            else:
                print("error")

    #鼠标抬起时,结束绘制，固定图形
    elif (event & cv2.EVENT_LBUTTONUP == cv2.EVENT_LBUTTONUP):
        is_mouse_down = False
        #把最终图形保存到备份画布
        img_backup = img.copy()
# 创建窗口
cv2.namedWindow('Draw Shapes', cv2.WINDOW_NORMAL)

# 设置鼠标回调
cv2.setMouseCallback('Draw Shapes',mouse_callback,"001")


while True:
    #显示图像
    cv2.imshow('Draw Shapes',img)
    #等待按键
    key = cv2.waitKey(1) & 0xFF
    if (key == ord('q')):#按q退出
        break
    elif (key == ord('l')):
         currentshape = 0    
    elif (key == ord('r')):
         currentshape = 1
    elif (key == ord('c')):
         currentshape = 2
  
cv2.destroyAllWindows()
