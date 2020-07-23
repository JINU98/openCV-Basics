import cv2
import numpy as np

cap=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output.avi',fourcc,200,(640,480))
while True:
	ret,frame=cap.read(0)
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	out.write(frame)
	cv2.imshow('frame',frame)
	cv2.imshow('gary',gray)
	if cv2.waitKey(50) & 0XFF == ord('q'):
		break
cap.release()
out.release()
cv2.destroyALLWindows()