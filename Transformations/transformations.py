import numpy as np 
import cv2

cap=cv2.VideoCapture(0)
while True:
	_,frame=cap.read()
	hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

	#detect except white
	# low = np.array([0, 42, 0])
	# high = np.array([179, 255, 255])

	lower_red=np.array([161,155,84])
	upper_red=np.array([179,255,255])

	mask=cv2.inRange(hsv,lower_red,upper_red)
	res=cv2.bitwise_and(frame,frame,mask=mask)

	kernel=np.ones((5,5),np.uint8)
	erosion=cv2.erode(mask,kernel,iterations=1)
	dialation=cv2.dilate(mask,kernel,iterations=1)

	opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
	closing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)

	cv2.imshow('frame',frame)
	cv2.imshow('res',res)
	cv2.imshow('kernel',kernel)
	cv2.imshow('erosion',erosion)
	cv2.imshow('dialation',dialation)
	cv2.imshow('opening',opening)
	cv2.imshow('closing',closing)



	k=cv2.waitKey(5) & 0xFF
	if k==2:
		break;