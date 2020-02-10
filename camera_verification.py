###Alex Stephens, Jared Homer, Tracey Gibson

import cv2
import numpy as np

FILE_NAME = "CameraParams.txt"
# File IO
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

# Intrinsics matrix K
K = np.array(data[6:9])

priPoint = np.array(data[1])  # unit=pixels

# Assuming you calibrated using 20 images, using first image as world coord frame
extRotMatrix = np.array(data[9:12][:])
extTransVect = np.array(data[69:72][:])

# Extrinsics matrix for world to camera frame
extMatrix = np.concatenate((extRotMatrix, np.transpose(extTransVect)), axis=0)

Z = 520.7  # mm away from camera

# origin transformed from world to camera frame
origin_world = np.array([0,0,0,1])
intermed_mat = np.dot(extMatrix, K)/Z
origin_cam = np.dot(origin_world, intermed_mat)

# matrix for camera to world calculations
inv_intermed_mat = np.linalg.pinv(intermed_mat)

def onMouse(event, r, c, flags, param):  #Grabs mouse input and returns pixel coordinates (r,c) and image coordinates (u,v)
    if event == cv2.EVENT_LBUTTONDOWN:
        rcCoords = np.array([r, c, 1])

        worldCoords = np.dot(rcCoords, inv_intermed_mat)
        print("World Coordinates")
        print("(" + str(worldCoords[0]) + ", " + str(worldCoords[1]) + ")")
        cv2.circle(picture, (int(rcCoords[0]), int(rcCoords[1])), 3, (0, 255, 0), thickness=-1)
        cv2.putText(picture, "(" + str(round(worldCoords[0], 2)) + "," + str(round(worldCoords[1],2)) + ")",
                    (int(rcCoords[0] - 30), int(rcCoords[1] - 10)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 255, 0))

        cv2.imshow("picture", picture)

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
# Commented out if using capture from video
# Uncomment if using file Image1.png, the first image from MATLAB's calibrator
picture = cv2.imread("Image1.png")  # for testing using the image used to determine world frame
while not escape:
    cv2.imshow('picture', picture)
    cv2.setMouseCallback('picture', onMouse)  #Ties onMouse function to 'picture' window

    key = cv2.waitKey(0)
    if key == 27:
        print('Pressed esc')
        escape = True
cv2.destroyAllWindows()
