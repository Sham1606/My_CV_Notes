import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('Cat',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#Laplacian

lap = cv.Laplacian(img, cv.CV_64F) # here it will the take gray image
lap = np.uint8(np.absolute(lap)) # the output may contain negative values due to the nature of the operator. However, when displaying the image, negative values are not meaningful, as image data is typically represented using unsigned integers.
# is used to take the absolute value of all elements in the array lap, ensuring that all values are positive.
cv.imshow('Laplacian', lap)

# Sobel

sobelX = cv.Sobel(img, cv.CV_64F, 1, 0)
sobelY = cv.Sobel(img, cv.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))
sobelCombined = cv.bitwise_or(sobelX, sobelY)

cv.imshow("Sobel X", sobelX)
cv.imshow("Sobel Y", sobelY)
cv.imshow("Soblel Combined", sobelCombined)


cv.waitKey(0)