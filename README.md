# camera_verifications.py
## CameraParams_totxt.m (Requries MATLAB R2019b!)
* The .m file assumes that you have used the MATLAB Camera Calibration and have selected "Export Parameters to Workspace." 

Running this script will create a .txt file (CameraParams.txt) that will be read in by camera_verifications.py. This .txt file contains all of the Camera Parameters exported by the MATLAB Camera Calibration, including the Extrinsic Properties of all the images taken during calibration.

## camera_verifications.py (Requires OpenCV2 and numpy)
* This script assumes that you have selected an image to represent your world frame (By default image 1), and have measured the Z distance to this frame from your camera.
* You must change the Z value in the code if you wish to use your own Z value and image capture.
* For testing purposes, you may wish to use the CameraParams.txt and Image1.png. If you wish to do so, you must uncomment line 79 in the python script, camera_verifications.py

Running this script will open a live webcam feed that will grab an image when Esc is pressed. The image grabbed will then be displayed, allowing the user to select points represented in the image frame. These points will be plotted onto the image, with their coordinates in the World Frame outputted to the python console window.
