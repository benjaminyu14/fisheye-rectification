#this is testing the combination of distort and undistort
#add multi-threading inorder to undisort images real time
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
num_images = int(input("How many images do you want?: "))

def images():
    camera = PiCamera()
    time.sleep(1)
    camera.resolution = (1280, 1024)
    camera.vflip = True
    camera.hflip = True
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
    
    
#the following is undistort

def undistortion():
    t1.join()
    DIM=(1280, 1024)
    K=np.array([[288.23012604283355, 0.0, 623.634604791886], [0.0, 286.7591721598898, 504.3570814118297], [0.0, 0.0, 1.0]])
    D=np.array([[0.08146352938392548], [-0.0005017125365272613], [-0.007533972595132653], [-0.01029744592250182]])

    def undistort(img_path, output_path):
        images = glob.glob(img_path+'/*.jpg')
        print("images: ", images)
        for img_path in images:
            print("img_path: ", img_path)
            c = int(img_path.split("_")[1].split(".")[0])
            img_path_array=img_path.split('/')
            img_output_path=img_path_array[1]
            img = cv2.imread(img_path)
            print('print images', img)
            h, w = img.shape[:2]
            map1, map2 = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, DIM, cv2.CV_16SC2)
            undistorted_img = cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
            cv2.imshow("undistorted", undistorted_img)
            cv2.imwrite(output_path+"/frame_"+ ("{:03d}".format(c)) + ".jpg", undistorted_img)

    if __name__ == '__main__':
        #input_image_folder_name = sys.argv[1]
        #output_image_folder_name = sys.argv[2]
        input_image_folder_name = input_folder
        output_image_folder_name = output_folder
        undistort(input_image_folder_name, output_image_folder_name)

t1 = Thread(target = images)
t2 = Thread(target = undistortion)

t1.start()
t2.start()

