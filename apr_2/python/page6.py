import numpy as np
import cv2 as cv

image = cv.imread('/tmp/sachin.jpg')
print(image)

# 190, 270                      360, 270
#
#
# 190, 330                      360, 330

# extract the feature
#              y1: y2,  x1: x2
# goggle = image[270:330, 190:360]

# modify the image
# image[0:100, 100:200] = (0, 0, 255)

# cv.rectangle(image, (190, 270), (360, 330), color=(0, 255, 255), thickness=-1)

cv.imshow('sachin', image)
# cv.imshow('goggle', goggle)

cv.waitKey(0)
cv.destroyAllWindows()
