# fisheye-rectification

This repository can be used to undistort individual frames that can be reassembled into a video.

1. Print pattern.png onto paper and take about 10-15 pictures of the chessboard pattern with your camera. Vary the position/angle of the camera between sample pictures. Place these pictures into and input folder. See the input folder for example pictures.
2. Run calibrate.py. Be sure to specify the image path in calibrate.py to your input folder. calibrate.py will output your camera's K and D constants and DIM.
3. Edit undistorted_frames.py and replace the K, D, and DIM values with your camera's respective values. Run undistorted_frames.py. You will be prompted with input and output folders names to create. Your input folder contains the raw frames. Your output folder contains the undistorted frames. You will be prompted with how many frames you want to take. To achieve desired fps, adjust time.sleep() in undistorted_frames.py; def images()
4. Check your input and output folders for successful frames.
5. (If you want to assemble to video mp4 format): Install ffmpeg (pip3 install ffmpeg). In terminal, enter: ffmpeg -framerate 4 -pattern_type glob -i '/path/to/folder/*.jpg' -c:v libx264 -crf 18 -pix_fmt yuv420p output.mp4            <--- basic edits: framerate value, input path, video_file_name.mp4
