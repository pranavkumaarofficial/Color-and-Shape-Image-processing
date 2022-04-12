# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 19:26:31 2022

@author: Pranav
"""


import numpy as np
import cv2

a=[]
res=[] #stores final result 


#Shape Detection 

def AddToList(a,ele):
    a.append(ele)

def AppendLists(b,a):
    b.append(a)




global imageFrame

    
def ColorDetection():
 
    global imageFrame

    #imageFrame = cv2.imread("C:\\Users\\Pranav\\Desktop\\SkillDev\\IEEE CS\\Image Processing\\ieee1.jpeg")  

    # Convert the imageFrame in 
    # BGR(RGB color space) to 
    # HSV(hue-saturation-value)
    # color space
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)
  
    # Set range for red color and 
    # define mask
    red_lower = np.array([136, 87, 111], np.uint8)
    red_upper = np.array([180, 255, 255], np.uint8)
    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)
  
    # Set range for green color and 
    # define mask
    green_lower = np.array([36, 50, 70], np.uint8)
    green_upper = np.array([89, 255, 255], np.uint8)
    green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)
  
    # Set range for blue color and
    # define mask
    blue_lower = np.array([94, 80, 2], np.uint8)
    blue_upper = np.array([120, 255, 255], np.uint8)
    blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)
    
    
    # Set range for orange color and 
    # define mask
    orange_lower = np.array([18, 40, 90], np.uint8)
    orange_upper = np.array([24, 255, 255], np.uint8)
    orange_mask = cv2.inRange(hsvFrame, orange_lower, orange_upper)
    
    # Set range for yellow color and 
    # define mask
    yellow_lower = np.array([25, 50, 70], np.uint8)
    yellow_upper = np.array([35, 255, 255], np.uint8)
    yellow_mask = cv2.inRange(hsvFrame, yellow_lower, yellow_upper)
    
    # Morphological Transform, Dilation
    # for each color and bitwise_and operator
    # between imageFrame and mask determines
    # to detect only that particular color
    kernal = np.ones((5, 5), "uint8")
      
    # For red color
    red_mask = cv2.dilate(red_mask, kernal)
    #res_red = cv2.bitwise_and(imageFrame, imageFrame, 
   #                           mask = red_mask)
      
    # For green color
    green_mask = cv2.dilate(green_mask, kernal)
   # res_green = cv2.bitwise_and(imageFrame, imageFrame,
   #                             mask = green_mask)
      
    # For blue color
    blue_mask = cv2.dilate(blue_mask, kernal)
   # res_blue = cv2.bitwise_and(imageFrame, imageFrame,
       #                        mask = blue_mask)
   
    # For orange color
    orange_mask = cv2.dilate(orange_mask, kernal)
   # res_orange = cv2.bitwise_and(imageFrame, imageFrame,
                   #            mask = orange_mask)
    # For yellow color
    yellow_mask = cv2.dilate(yellow_mask, kernal)
   #res_yellow = cv2.bitwise_and(imageFrame, imageFrame,
                              # mask = yellow_mask)

    #############
    # Creating contour to track red color
    contours, hierarchy = cv2.findContours(red_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
      
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            
              
            cv2.putText(imageFrame, "Red Colour", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                        (0, 0, 255))    
  
        color="Red"
        return color
    
    #############
    # Creating contour to track green color
    contours, hierarchy = cv2.findContours(green_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
      
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
           
              
            cv2.putText(imageFrame, "Green Colour", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 
                        1.0, (0, 255, 0))
  
        color="Green"
        return color
    
     # Creating contour to track orange color
    contours, hierarchy = cv2.findContours(orange_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
      
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            
              
            cv2.putText(imageFrame, "Orange Colour", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                        (0, 0, 255))   
    
        color="Orange"
        return color
    
    #############
    # Creating contour to track blue color
    contours, hierarchy = cv2.findContours(blue_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)

    
    
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
     
            cv2.putText(imageFrame, "Blue Colour", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.0, (255, 0, 0))
       
         
        color="Blue"
        return color   
            
 # Creating contour to track yellow color
    contours, hierarchy = cv2.findContours(yellow_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
      
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
           
              
            cv2.putText(imageFrame, "Yellow Colour", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                        (0, 0, 255))   


        color="Yellow"
        return color
    
##############################################################################################
    
    
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
    l1=list((x,y))
    AddToList(a, l1) #Should be done at the end
    
    
    
    
    approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 5
    
    k=ColorDetection()
    #print(k)
    AddToList(a, k)
            
    if len(approx) == 3:
        cv2.putText( img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0) )
    elif len(approx) == 4 :
        x, y , w, h = cv2.boundingRect(approx)
        aspectRatio = float(w)/h
        #print(aspectRatio)
        
        
        if aspectRatio >= 0.95 and aspectRatio < 1.05:
            cv2.putText(img, "square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
            AddToList(a, "Square")
        else:
            cv2.putText(img, "rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
            AddToList(a, "Rectangle")
            
    elif len(approx) == 5 :
        cv2.putText(img, "pentagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        AddToList(a, "Pentagon")
    elif len(approx) == 10 :
        cv2.putText(img, "star", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        AddToList(a, "Star")
    else:
        cv2.putText(img, "circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        AddToList(a, "Circle")
        
    print(a)
        
AppendLists(res, a) 
     
     
cv2.imshow('shapes', img)

cv2.waitKey(0)
cv2.destroyAllWindows()