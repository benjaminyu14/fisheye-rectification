# fisheye-rectification

This repository can be used to undistort individual frames that can be reassembled into a video.

1. Print pattern.png onto paper and take about 10-15 pictures of the chessboard pattern with your camera. Vary the position/angle of the camera between sample pictures. Place these pictures into and input folder. See the input folder for example pictures.
2. Run calibrate.py. Be sure to specify the image path in calibrate.py to your input folder. calibrate.py will output your camera's K and D constants and DIM.
3. 
