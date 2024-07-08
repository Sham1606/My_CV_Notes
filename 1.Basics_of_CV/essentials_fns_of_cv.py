import cv2 as cv

img = cv.imread('Photos/park.jpg')
cv.imshow('Park',img)

# Converting to gray scale
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray_img)

# Blurring
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade for aking the edges which is visible
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

#Dilating the image
dilated = cv.dilate(canny, (3,3), iterations=1) # the second parameter will take the detailing that how much it can draw from the available datasource
cv.imshow('Dilated',dilated)

# Eroding the image, the more detailed and the edges have more thickness
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded',eroded)

# Resize the image
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Cropping 
cropped = img[50:200, 200:400] # it is like slicing the first will be hei
cv.imshow('Cropped', cropped)


cv.waitKey(0)