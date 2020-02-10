###Alex Stephens, Jared Homer, Tracey Gibson

import cv2
import numpy as np

FILE_NAME = "CameraParams.txt"

input_file = open(FILE_NAME, 'r')
data = []
current_data = []

for data_line in input_file:
    line = data_line.strip()
    if not line.startswith('#'):
        input_data = data_line.rstrip().split()
        for val in input_data:
            current_data.append(float(val))
        data.append(current_data)
        current_data = []

input_file.close()

K = np.array(data[6:9])

focalLength = np.array(data[0])  # unit=pixels
priPoint = np.array(data[1])  # unit=pixels

# Assuming you calibrated using 20 images, using first image as world coord origin
extRotMatrix = np.array(data[9:12][:])
extTransVect = np.array(data[69:72][:])

extMatrix = np.concatenate((extRotMatrix, np.transpose(extTransVect)), axis=0)

Z = 444.5

# origin transformed from world to camera frame
origin_world = np.array([0,0,0,1])
origin_cam = np.dot(origin_world, np.dot(extMatrix, K))/Z

# change extMatrix to extMatrix for camera to world frame
extRotMatrix = np.concatenate((np.transpose(extRotMatrix), np.zeros((3,1))), axis=1)
extRotMatrix = np.concatenate((extRotMatrix, np.array([[0,0,0,1]])), axis=0)
transMatrix = np.concatenate((np.identity(3), -extTransVect), axis=1)
transMatrix = np.concatenate((transMatrix, np.array([[0,0,0,1]])), axis=0)
extMatrix = np.dot(extRotMatrix, transMatrix)

magFocalLength = np.linalg.norm(focalLength)  #Lambda in World Units
pixelHeight = np.array(focalLength[:] / magFocalLength)  #Pixel Heights Sx and Sy in World Units

def onMouse(event, r, c, flags, param):  #Grabs mouse input and returns pixel coordinates (r,c) and image coordinates (u,v)
    global rcCoords, uvCoords
    if event == cv2.EVENT_LBUTTONDOWN:
        rcCoords = np.array([r,c])
        uvCoords = np.subtract(priPoint, rcCoords)
        uvCoords = np.divide(uvCoords, focalLength)
        uvCoords = np.append(uvCoords, 1)
        xyCoords = uvCoords * Z
        xyCoords = np.append(xyCoords, 1)
        xyCoords = xyCoords.reshape((4,1))
        worldCoords = np.dot(extMatrix, xyCoords)
        print("World Coordinates")
        print(worldCoords)  # INCORRECT VALUES

capture = cv2.VideoCapture(0)
print('Press ESC to Grab Image')
escape = False
while not escape:  #Displays webcam feed and saves the last frame before ESC is pressed
    has_frame, frame = capture.read()
    if not has_frame:
        print('Can\'t get frame')
        break
    cv2.circle(frame, (int(origin_cam[0]), int(origin_cam[1])), 5, (255,0,0), thickness=-1)
    cv2.putText(frame, "World Origin", (int(origin_cam[0] - 25), int(origin_cam[1] - 10)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.25, (255,0,0))
    cv2.circle(frame, (int(priPoint[0]), int(priPoint[1])), 5, (0,0,255), thickness=-1)
    cv2.putText(frame, "Principal Pt", (int(priPoint[0] - 25), int(priPoint[1] - 10)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.25, (0, 0, 255))
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



