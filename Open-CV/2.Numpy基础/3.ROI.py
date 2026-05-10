import numpy as np
import cv2

img = np.zeros((600,600,3),np.uint8)
roi = img[100:400,100:500]

# Blue
#   y,x
roi[:,:] = [255,0,0]
# Green
roi[10:300,10:300] = [0,255,0]

cv2.imshow('img',roi)
key = cv2.waitKey(0)

if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()