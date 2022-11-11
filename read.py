import sys
import numpy as np
import cv2
lower=np.array([30,100,100])
upper=np.array([80,255,255])
blank=np.zeros((500,500,3), dtype='uint8')
cap=cv2.VideoCapture(0) 
while True:
    ret,frame=cap.read()
    cv2.imshow('frame',frame)
    resized = cv2.resize(frame,[500,500], interpolation = cv2.INTER_AREA)
    if cv2.waitKey(1)==ord('q'):
        break
    cvt_img=cv2.cvtColor(resized,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(cvt_img,lower,upper)
    cv2.imshow('mask',mask)
    coords = np.column_stack(np.where(mask >0))    
    countl=0
    countm=0
    countr=0
    for i in coords:
        if i[1]<resized.shape[1]//3 :
            countl+=1
        elif i[1]>2*resized.shape[1]//3:
            countr+=1
        else:
            countm+=1
    if(countl>=50):
        print('l--')
    else:
        print('>f<')
        
cap.release()
cv2.destroyAllWindows()