# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 11:44:55 2020

@author: asus
"""

import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

image = cv.imread("G:/computer_vision/blue_background_image.jpg")

print(type(image), image.shape)

image_copy = np.copy(image)
image_copy = cv.cvtColor(image_copy, 
                         cv.COLOR_BGR2RGB)

image_copy_HSV = cv.cvtColor(image_copy, 
                             cv.COLOR_RGB2HSV)
#plt.imshow(image_copy_HSV)

#define the color threshold for blue backgroung in RGB

lower_color = np.array([0,0,70])
upper_color = np.array([100,100,255])

#define the color threshold for blue backgroung in HSV

lower_color_HSV = np.array([10,100,100])
upper_color_HSV = np.array([60,255,255])

#creat mask

mask = cv.inRange(image_copy, lower_color, 
                  upper_color)

#mask = cv.inRange(image_copy_HSV, lower_color_HSV, 
#                  upper_color_HSV)

#plt.imshow(mask, cmap='gray')

masked_image = np.copy(image_copy)

# select the background in origin image to become disappeared
#masked_image[mask != 0] = [0, 0, 0]

# select the ballon in origin image to become disappeared
masked_image[mask == 0] = [0, 0, 0]
plt.imshow(masked_image)

#add new background

background_image = cv.imread("G:/computer_vision/background.jpeg")
background_image = cv.cvtColor(background_image, 
                               cv.COLOR_BGR2RGB)

crop_background = background_image[0:183, 
                                   0:275]
crop_background[mask == 0] = [0, 0, 0]
#plt.imshow(crop_background)

full_image = masked_image + crop_background
#plt.imshow(full_image)
