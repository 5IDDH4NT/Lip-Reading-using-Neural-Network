import cv2
import numpy as np
import os
from os.path import isfile, join


video_cap = cv2.VideoCapture(r'input/ExcuseMe.MP4')
output_path = 'output/'
casPath = os.path.dirname(cv2.__file__)+"/data/haarcascade_frontalface_default.xml"
faceCascade= cv2.CascadeClassifier(casPath)

def getFrame(second):
    
    video_cap.set(cv2.CAP_PROP_POS_MSEC, second * 1000)
    hasFrame, frames = video_cap.read()
    face= faceCascade.detectMultiScale(frames, scaleFactor=1.1, minNeighbors=5, 
    minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

    for (x, y,w,h) in face:
        cv2.rectangle(frames,(x,y),(x+w, y+h), (0,255,0),2)
    if hasFrame:
        cv2.imwrite(output_path + 'image' + str(count) + '.jpg', frames)
        

    return hasFrame

sec = 0
frameRate = 0.25
count = 1
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)

