###Alex Stephens, Jared Homer
import cv2
import numpy as np

capture = cv2.VideoCapture(0)
print('Press ESC to Grab Image')
escape = False
while not escape:  #Part 1
    has_frame, frame = capture.read()
    if not has_frame:
        print('Can\'t get frame')
        break
    cv2.imshow('Press ESC to Grab Image', frame)

    key = cv2.waitKey(3)
    if key == 27:
        print('Pressed esc')
        picture = frame
        escape = True
capture.release()
cv2.destroyAllWindows()

cv2.imshow('picture', picture)
cv2.waitKey(0)

