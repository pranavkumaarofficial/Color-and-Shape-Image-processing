
"""
Created on Mon Apr  4 17:16:47 2022

@author: Pranav
"""

import cv2
def nothing(x):
    pass
cap = cv2.VideoCapture(0)
import numpy as np
cv2.namedWindow("Trackbars")
cv2.createTrackbar("Blur", "Trackbars", 0, 20, nothing)

while True:
  
    ret, frame = cap.read()
    image = cv2.flip( frame, 1 ) 
    l_h = cv2.getTrackbarPos("Blur", "Trackbars")
    l_h=(2*l_h)+1 #2x+1 makes it an odd number 
   
   
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #converting to gray 
    blur=cv2.GaussianBlur(image,(l_h,l_h),cv2.BORDER_DEFAULT) #takes odd numbers only
    img_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR) 
    stacked = np.hstack((image,blur,img_bgr)) #stacking all 3 frames to one window 
    
 
    cv2.imshow('Trackbars',cv2.resize(stacked,None,fx=0.8,fy=0.8))
 
    key = cv2.waitKey(1)
    if key == 27:
        break
    
   
cap.release()
cv2.destroyAllWindows()