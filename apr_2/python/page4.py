import numpy as np
import cv2 as cv

# create a black canvas with 1024x1024
canvas = np.zeros((1024, 1024, 3))

# draw a rectangle
# RGB => BGR
# Haar
cv.rectangle(canvas, (100, 100), (350, 300), color=(255, 0, 0), thickness=2)
cv.rectangle(canvas, (150, 150), (200, 200), color=(0, 255, 255), thickness=2)
cv.rectangle(canvas, (250, 150), (300, 200), color=(0, 255, 255), thickness=2)

cv.imshow('canvas', canvas)
cv.waitKey(0)