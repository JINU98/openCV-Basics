import numpy as np 
import cv2

img=cv2.imread('midoriya_1.jpg',cv2.IMREAD_COLOR)
midoriya_face=img[200:300,250:400]
img[0:100,0:150]=midoriya_face
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()