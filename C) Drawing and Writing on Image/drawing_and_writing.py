import cv2
import numpy as np

img = cv2.imread('midoriya_1.jpg',cv2.IMREAD_COLOR)
cv2.line(img,(0,0),(150,150),(255,255,255),10)
cv2.imshow('image',img)

cv2.rectangle(img,(50,0),(400,400),(0,255,0),5)
cv2.circle(img,(100,63),55,(0,0,255),-1)

pts=np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
cv2.polylines(img,[pts],True,(0,255,255),3)

font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Midoriya',(0,430),font,1,(200,255,255),2,cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()