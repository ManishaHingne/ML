import numpy as np
import cv2 as cv

# open web camera
capture = cv.VideoCapture(0)

# infinite loop
while True:
    returnVal, image = capture.read()

    cv.rectangle(image, (100, 100), (350, 300), color=(255, 0, 0), thickness=2)
    cv.rectangle(image, (150, 150), (200, 200), color=(0, 255, 255), thickness=2)
    cv.rectangle(image, (250, 150), (300, 200), color=(0, 255, 255), thickness=2)

    cv.imshow('original capture', image)

    # check if user presses the q
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# release the web camera
capture.release()
cv.destroyAllWindows()
