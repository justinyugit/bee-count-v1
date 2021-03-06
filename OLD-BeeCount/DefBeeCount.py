#960x720
from matplotlib import pyplot as plt
import numpy as np
import cv2
import sys
import csv

cap = cv2.VideoCapture('/home/justin/Downloads/vid.h264')
fgbg=cv2.bgsegm.createBackgroundSubtractorMOG()
xcnts = []
dev_x=np.array([])

dev_yR=np.array([])
dev_yL=[]


def PROCESS(type):
    
        
    frames=0
    while(frames<2000):
        ret, frame = cap.read()
        if (type=="left"):
            roi=frame[250:450, 0:420]
        if (type=="right"):
            roi=frame[250:450, 540:960]
            
        fgmask = fgbg.apply(roi)
    
        cv2.imshow('frame', fgmask)
        cv2.imshow('actual', roi)
        cnts = cv2.findContours(fgmask, cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[-2]
        s1=5
        s2=400
        for cnt in cnts:
            if s1<cv2.contourArea(cnt)<s2:
                xcnts.append(cnt)
            

        print(len(xcnts))
        frames=frames+1
        if len(xcnts)<200 and type=="left":
            dev_yL.append(len(xcnts))
                
            #np.append(dev_x,frames/1500)
            #np.append(dev_yL,len(xcnts))
        elif len(xcnts)<200 and type=="right":
            np.append(dev_x,frames/1500)
            np.append(dev_yL,len(xcnts))
        elif len(xcnts)>=200 and type=="left":
            print("too high")
            dev_yL.append(0)
            #np.append(dev_x,frames/1500)
            #np.append(dev_yL,0)
        elif len(xcnts)>=200 and type=="right":
            np.append(dev_x,frames/1500)
            np.append(dev_yR,0)
    
    
        xcnts.clear()
        k = cv2.waitKey(1) & 0xff
        if k == ord('c'):
            break



PROCESS("left")

with open('YL.csv', 'w') as left_file:
    csv_writer = csv.writer(left_file)
    csv_writer.writerow(dev_yL)
#PROCESS("right")
plt.plot(dev_x, dev_yL)
plt.plot(dev_x, dev_yR)
plt.xlabel('Seconds since start')
plt.ylabel('Number of bees')
plt.show()
