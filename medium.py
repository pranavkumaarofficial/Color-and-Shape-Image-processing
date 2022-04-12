# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 18:55:52 2022

@author: Pranav
"""

import numpy as np
import cv2

#Shape Detection 

def AddToList(a,ele):
    a.append(ele)

def AppendLists(b,a):
    b.apend(a)
    
    
    
    
img = cv2.imread('C:\\Users\\Pranav\\Desktop\\SkillDev\\IEEE CS\\Image Processing\\ieee1.jpeg')
imgGry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thrash = cv2.threshold(imgGry, 240 , 255, cv2.CHAIN_APPROX_NONE)
contours , hierarchy = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)



for contour in contours:
    
    
    # finding center point of shape
    M = cv2.moments(contour)
    if M['m00'] != 0.0:
    		x = int(M['m10']/M['m00'])
    		y = int(M['m01']/M['m00'])
    #l1=list((x,y))
    #AddToList(a, l1) #Should be done at the end
    
    
    
    
    approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 5
    
    
    if len(approx) == 3:
        cv2.putText( img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0) )
    elif len(approx) == 4 :
        x, y , w, h = cv2.boundingRect(approx)
        aspectRatio = float(w)/h
        print(aspectRatio)
        
        
        if aspectRatio >= 0.95 and aspectRatio < 1.05:
            cv2.putText(img, "square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

        else:
            cv2.putText(img, "rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

    elif len(approx) == 5 :
        cv2.putText(img, "pentagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 10 :
        cv2.putText(img, "star", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    else:
        cv2.putText(img, "circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        
        
        
cv2.imshow('shapes', img)

cv2.waitKey(0)
cv2.destroyAllWindows()