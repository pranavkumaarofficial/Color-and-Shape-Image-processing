# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 16:45:15 2022

@author: Pranav
"""
#greyscale
import cv2 
img = cv2.imread('C:\\Users\\Pranav\\Desktop\\SkillDev\\IEEE CS\\Image Processing\\ieee1.png')     
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
cv2.imshow('Grayscale', gray_image)
cv2.waitKey() 
cv2.destroyAllWindows()