import numpy as np
import cv2 as cv

# open web camera
capture = cv.VideoCapture(0)

# infinite loop
while True:
    returnVal, image = capture.read()

    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow('original capture', image)
    cv.imshow('gray capture', gray)

    # check if user presses the q
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# release the web camera
capture.release()
cv.destroyAllWindows()
