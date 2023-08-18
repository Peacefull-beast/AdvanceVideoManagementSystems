
# analytics.py
import cv2
import numpy as np
import subprocess

# url list of camera
urls = [
    0,0,0,0,0,0,0,0,0
]

# Create OpenCV video capture objects for all cameras
caps = [cv2.VideoCapture(url) for url in urls]
# The function to launch the video player and execute analytics can be moved here.

def vedio(nummain, analytics):
    file_path=analytics+".py"
    exec(open(file_path).read())
    
    
