import numpy as np
import cv2 as cv

# read the colorful image
# image = cv.imread('/tmp/iphone.png', 0)

image = cv.imread('/tmp/iphone.png')
cv.imshow('colorful', image)

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

cv.waitKey(0)