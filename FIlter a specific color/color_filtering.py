import numpy as np 
import cv2

cap=cv2.VideoCapture(0)
while True:
	_,frame=cap.read()
	hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

	#detect except white
	low = np.array([0, 42, 0])
	high = np.array([179, 255, 255])

	lower_red=np.array([161,155,84])
	upper_red=np.array([179,255,255])

	mask=cv2.inRange(hsv,lower_red,upper_red)
	res=cv2.bitwise_and(frame,frame,mask=mask)

	cv2.imshow('frame',frame)
	cv2.imshow('mask',mask)
	cv2.imshow('res',res)

	k=cv2.waitKey(5) & 0xFF
	if k==2:
		break;
cv2.destroyALLWindows()
cap.relase()
