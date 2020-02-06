###Alex Stephens, Jared Homer

import cv2
import numpy as np

FILE_NAME = "CameraParams.txt"



input_file = open(FILE_NAME, 'r')
data = []
current_data = []

for data_line in input_file:
    line = data_line.strip()
    if not line.startswith('#'):
        input_data = data_line.rstrip()
        input_data = input_data.split()
        for val in input_data:
            current_data.append(float(val))
        data.append(current_data)
        current_data = []

input_file.close()

focalLength = np.array(data[0])  # unit=pixels
priPoint = np.array(data[1])  # unit=pixels

#priPoint = np.array([349.3, 257.05])  #Test Values, unit=pixels
#focalLength = np.array([643.4886, 644.3349])  #Test Values, unit=pixels

magFocalLength = np.linalg.norm(focalLength)  #Lambda in World Units
pixelHeight = np.array(focalLength[:] / magFocalLength)  #Pixel Heights Sx and Sy in World Units

def onMouse(event, r, c, flags, param):  #Grabs mouse input and returns pixel coordinates (r,c) and image coordinates (u,v)
    global pixCoord, imCoord
    if event == cv2.EVENT_LBUTTONDOWN:
        pixCoord = np.array([r,c])
        #imCoord = (priPoint[0] - pixCoord[0],  priPoint[1] - pixCoord[1])
        #imCoord = np.subtract(priPoint,pixCoord)  unnecessary
        #camCoordOverZ = np.divide(imCoord,focalLength)  #x/z and y/z unnecessary
        Z = 127 #Z in mm
        #camCoord = camCoordOverZ * Z  unnecessary
        print("Principal Point:", priPoint[:])  # For Testing
        print("Coordinates in Pixel Frame:", pixCoord[:]) #For Testing
        #print("Coordinates in Image Frame:",  imCoord[:])  # For Testing unnecessary
        #print("Coordinates in Camera Frame:", camCoord[:])  # For Testing unnecessary

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
escape = False
while not escape:
    cv2.imshow('picture', picture)
    cv2.setMouseCallback('picture', onMouse)  #Ties onMouse function to 'picture' window
    key = cv2.waitKey(0)
    if key == 27:
        print('Pressed esc')
        escape = True
cv2.destroyAllWindows()



