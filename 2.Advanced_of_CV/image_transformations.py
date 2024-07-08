import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('Park',img)

# Translation 
def translate(img, x, y): # (x, y) -> no. of pixels u want to translate
    transMat = np.float32([[1, 0, x], [0, 1, y]]) # translation matrix
    dimensions = (img.shape[1], img.shape[0]) # parameter 1 -> width, parameter 2 -> height
    return cv.warpAffine(img, transMat, dimensions)

# -ve x --> Left
# -ve y --> Up
# +ve x --> Right
# +ve y --> Down

translated = translate(img, -100, 100)
cv.imshow('Translated', translated)

# Rotation

def rotate(img, angle, rotPoint = None):
    (height, width) = img.shape[:2] # first two values
    
    if rotPoint is None: # if rotation is none it will be assigned to center
        rotPoint = (width//2, height//2) 
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45)
cv.imshow('Rotated', rotated)

# Resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# flipping

flip = cv.flip(img, 0)  
cv.imshow('Flipped', flip)

# 0 -> flip vertically
# 1 -> flip horizontally
# -1 -> flip both vertically and horizontally

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
                         