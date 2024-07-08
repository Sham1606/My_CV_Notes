import cv2 as cv

# way of reading images in cv2
img  = cv.imread('Photos/cat_large.jpg')

# ONCE the message has been read we are displaying it
cv.imshow('Cat', img)

cv.waitKey(0) # keyboard binding function, waits for a specific delay time in milliseconds time to be pressed