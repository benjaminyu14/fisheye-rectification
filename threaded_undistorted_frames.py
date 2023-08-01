#This is the multi-threaded version of undistorted_frames.py
#The number of pictures to undistort is divided between 4 threads to handle
#This script is 100% faster to execute than undistorted_frames.py
#Edit the multithreading section to add more threads if desired.
from picamera import PiCamera
from threading import Thread
import time
import cv2
import numpy as np
import sys
import uuid
import glob
import os

global input_folder 
input_folder = input("Name of input folder: ")
os.mkdir(input_folder)
global output_folder
output_folder= input("Name of output folder: ")
os.mkdir(output_folder)
global num_images 
num_images = int(input("How many images do you want? (Will only take multiples of 4): "))
num_images = num_images - (num_images%4)
global c
threads = []


def images():
    camera = PiCamera()
    time.sleep(1)
    camera.resolution = (1280, 1024)
    camera.vflip = True
    camera.hflip = True
    global c
    c = 1
    print("Entering while")
    while True:
        if c > num_images:
            break
        
        file_name = "/home/pi/Undistort_Fisheye_Images/undistort_fisheye_images/test/" + input_folder + "/img_" + str(c) + ".jpg"
        camera.capture(file_name)
        print("Frame " + str(c) + " captured")
        c += 1
        time.sleep(.0625)
    sys.exit() 
    
    

def undistortion(start, end):
    DIM=(1280, 1024)
    K=np.array([[288.23012604283355, 0.0, 623.634604791886], [0.0, 286.7591721598898, 504.3570814118297], [0.0, 0.0, 1.0]])
    D=np.array([[0.08146352938392548], [-0.0005017125365272613], [-0.007533972595132653], [-0.01029744592250182]])

    def undistort(img_path, output_path):
        for x in range(start, end + 1):
            base_filename = f"img_{x}.jpg"
            image = os.path.join(img_path, base_filename)
            img_path_array=image.split('/')
            img_output_path=img_path_array[1]
            img = cv2.imread(image)
            h, w = img.shape[:2]
            map1, map2 = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, DIM, cv2.CV_16SC2)
            undistorted_img = cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
            cv2.imshow("undistorted", undistorted_img)
            cv2.imwrite(output_path+"/frame_"+ ("{:03d}".format(x)) + ".jpg", undistorted_img)
            print("***Frame " + str(x) + " undistorted***")

    if __name__ == '__main__':
        input_image_folder_name = input_folder
        output_image_folder_name = output_folder
        undistort(input_image_folder_name, output_image_folder_name)


takeimages = Thread(target = images)
start = 1
multiple = int(num_images/4)
end = multiple

for i in range (4):
    threads.append(Thread(target = undistortion, args = (start, end,)))
    start += multiple
    end += multiple


print("ENTERING PROCESSES: ")
takeimages.start()
takeimages.join()
print("UNDISTORTING NOW")
for thread in threads:
    thread.start()


