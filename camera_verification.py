###Alex Stephens, Jared Homer
import cv2
import numpy as np

priPoint = np.array([349.3, 257.05])  #Test Values

def onMouse(event, r, c, flags, param):  #Grabs mouse input and returns pixel coordinates (r,c) and image coordinates (u,v)
    global pixCoord, imCoord
    if event == cv2.EVENT_LBUTTONDOWN:
        pixCoord = np.array([r,c])
        #imCoord = (priPoint[0] - pixCoord[0],  priPoint[1] - pixCoord[1])
        imCoord = np.subtract(priPoint,pixCoord)
        print(priPoint[:])  # For Testing
        print(pixCoord[:]) #For Testing
        print(imCoord[:])  # For Testing

capture = cv2.VideoCapture(0)
print('Press ESC to Grab Image')
escape = False
while not escape:  #Displays webcam feed and saves the last frame before ESC is pressed
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
cv2.setMouseCallback('picture', onMouse)  #Ties onMouse function to 'picture' window
key = cv2.waitKey(0)
if key == 27:
    print('Pressed esc')
    cv2.destroyAllWindows()


