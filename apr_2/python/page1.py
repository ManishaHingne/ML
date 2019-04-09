import numpy as np
import cv2 as cv

# read the image
image = cv.imread('/tmp/iphone.png')

# image -> is made up of array of pixels => channels => RGB
# print(image)
# print(type(image))
# print(image.shape)

# display image on the window
cv.imshow('original', image)

# wait till user uses any key
cv.waitKey(0)

