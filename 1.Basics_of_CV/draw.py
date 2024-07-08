import cv2 as cv
import numpy as np

# way to create a blank color image
blank_color = np.zeros((500, 500, 3), dtype='uint8')
# cv.imshow('Blank', blank_color)

# 1. Point the image a certain color
# blank_color[200:300, 300:400] = 0, 0, 255  # BGR color format: Green
# cv.imshow('Green', blank_color)

# 2. Draw a rectangle
# cv.rectangle(blank_color, (0,0),(blank_color.shape[1]//2, blank_color.shape[0]//2 ), (0,255,0), thickness=cv.FILLED) # second paranteses is (width, height), third paranthese is color format in BGR format
# cv.imshow('Rectangle', blank_color)

# 3. Draw a circle
# cv.circle(blank_color, (blank_color.shape[1]//2, blank_color.shape[0]//2 ), 40 ,(0,0,255), thickness=cv.FILLED) # third parameter is pixel
# cv.imshow('Circle', blank_color)

# 4. Draw a line
# cv.line(blank_color, (0,0), (blank_color.shape[1]//2, blank_color.shape[0]//2 ), (255,255,255), thickness=3) # third parameter is pixel
# cv.imshow('Line', blank_color)

# 5. Write text
# cv.putText(blank_color, 'Hello my name is python', (0, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2 # thickness) # second parameter is the text we want to write, third parameter is the sentence we want to start and end # next is font size 
# cv.imshow('Text', blank_color)

cv.waitKey(0)
