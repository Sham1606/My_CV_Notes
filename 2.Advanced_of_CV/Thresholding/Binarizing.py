"""

A thresholded image is a binary representation of an original image where each pixel is classified as either foreground (object of interest) or background based on a specified threshold value. 
The thresholding process converts a grayscale or color image into a binary image, where pixel values are set to either 0 (black) or 255 (white) depending on whether they meet certain criteria relative to the threshold value.
"""

import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray_img)

# Simple thresholding
threshold, thresh = cv.threshold(gray_img, 100, 255, cv.THRESH_BINARY) # 150 -> Threshold value 255 -> Maximum value 
cv.imshow('Simple Threshold', thresh)

# Inverse threshold
threshold, thresh_inv = cv.threshold(gray_img, 100, 255, cv.THRESH_BINARY_INV) # 150 -> Threshold value 255 -> Maximum value 
cv.imshow('Inverse Threshold', thresh_inv)

# Adaptive thresholding -> finds the optimal threshold value by itself
adaptive_thresh = cv.adaptiveThreshold(gray_img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 1) # 11 -> Block Values  1 -> any integer
cv.imshow('Adaptive Threshold', adaptive_thresh)


cv.waitKey(0)