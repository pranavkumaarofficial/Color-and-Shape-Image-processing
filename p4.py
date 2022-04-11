# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 16:46:55 2022

@author: Pranav
"""
#Gaussian blur
#from path in folder
import cv2 
img = cv2.imread("C:\\Users\\Pranav\\Desktop\\SkillDev\\IEEE CS\\Image Processing\\ieee1.png")  
res = cv2.GaussianBlur(img,(23,11),cv2.BORDER_DEFAULT) #border default has some default value - probably default 
cv2.imshow('result.jpg', res) 
cv2.waitKey() 
cv2.destroyAllWindows()