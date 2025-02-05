'''
#Requirement: opencv-python, tkinter 

# Usage instruction: 
Choose point (double click left mouse button) in the order leftUpper, RightUpper, LeftLower, RightLower
Click "c" in the keyword for confirmation
This is for two-chamber crylic transfer box, the dimension is 

two-chamber place preference
_________445mm___________
|                        |
|                        |
295mm                    |
|                        |
|________________________|


fish tank
_________500mm___________
|                        |
|                        |
250mm                    |
|                        |
|________________________|

water sink tank
_________480mm___________
|                        |
|                        |
|                        |
|                        |
480mm                    |
|                        |
|                        |
|                        |
|________________________|

self stim
_________250mm___________
|                        |
|                        |
180mm                    |
|                        |
|________________________|

Cross Maze Test


610 x 610 mm
            _ 
           | |
           | |
           | |
___________| |___________   
|__________   ___________| 
           | |
           | |                                                                                             
           | |
           |_|
           

water_searching_form_board

_________640mm___________
|                        |
|                        |
430mm                    |
|                        |
|________________________|


homeCage
_________280mm___________
|                        |
|                        |
180mm                    |
|                        |
|________________________|





The output video is 445 * 295 at 30fps, thus 1mm/pixel

Changes can be made, for "out" and the "pts2" for other behavior test

'''


import cv2
import numpy as np
#import matplotlib.pyplot as plt
import os
from math import hypot
from tkinter import Tk
from tkinter.filedialog import askopenfilenames


box_length = 500
box_width = 250
posList = []


def draw_circle(event,x,y,flags,param):
    global mouseX,mouseY
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img_raw,(x,y),1,(255,0,0),-1)
        mouseX,mouseY = x,y
        posList.append((x, y))  


root1 = Tk()
root1.withdraw()
filez = askopenfilenames(parent = root1, title = 'Choose file')
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
file_order = 0;
for fullFileName in root1.tk.splitlist(filez):
    print(fullFileName)
    filename = fullFileName
    (root, ext) =os.path.splitext(filename) 
    duration = 1  # second
    freq = 440  # Hz
    file_order +=1
    cap = cv2.VideoCapture(filename)
    i=0
    while i<2:
        i+=1
        ret, img_raw =cap.read() #start capture images from webcam
        if ret == False:
            break
    
        while i==1:
            cv2.namedWindow("image")
            cv2.setMouseCallback("image", draw_circle)
            #print(posList)
            posNp = np.array(posList) 
            cv2.imshow('image',img_raw)
            k = cv2.waitKey(20) & 0xFF
            if k == ord("r"):    
                ret, img_raw =cap.read()                                                                                                                                                                                      
                image = img_raw
            if k == ord("c"):
                break
     cap.release()    
cv2.destroyAllWindows()       

j=0
for fullFileName in root1.tk.splitlist(filez):
    j+=1
    filename = fullFileName
    print(filename)
    (root, ext) =os.path.splitext(filename) 
    cap = cv2.VideoCapture(filename)
    while not cap.isOpened():
        cap = cv2.VideoCapture(filename)
        #os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
        print("Can't load the file")
        break
    fps = cap.get(cv2.CAP_PROP_FPS)
    #print(fps)
    duration = 1  # second
    freq = 440  # Hz
   
    cap = cv2.VideoCapture(filename)
    width = int(cap.get(3))
    height = int(cap.get(4))

    font = cv2.FONT_HERSHEY_SIMPLEX
    out = cv2.VideoWriter(root+'_GeoTran.mp4',fourcc,fps,(box_length,box_width))
    while True:
        ret, img_raw =cap.read() #start capture images from webcam
        if ret == False:
            break
        img = img_raw
        rows,cols,ch = img.shape
        pts1 = np.float32(posList[(j-1)*4:(j*4)])
        pts2 = np.float32([[0,0],[box_length,0],[0,box_width],[box_length,box_width]])
        M = cv2.getPerspectiveTransform(pts1,pts2)
        dst = cv2.warpPerspective(img,M,(box_length,box_width))
        out.write(dst)          
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()