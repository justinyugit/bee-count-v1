from matplotlib import pyplot as plt
import numpy as np
import cv2
import sys
import csv


fgbg=cv2.bgsegm.createBackgroundSubtractorMOG()
xcnts = [0]
dev_x=[0]

dev_yR=[0]
dev_yL=[0]
frames=0
xyz=sys.argv[2]

def PROCESS(type):
    cap = cv2.VideoCapture(sys.argv[1])
        
    frames=0
    dev_x=[0]
    while(frames<29000):
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
        if len(xcnts)<40 and type=="left":
            dev_yL.append(len(xcnts))
                
            dev_x.append(frames/1500)
            
        elif len(xcnts)<40 and type=="right":
            dev_x.append(frames/1500)
            dev_yR.append(len(xcnts))
        elif len(xcnts)>=40 and type=="left":
            print("too high")
            dev_yL.append(0)
            dev_x.append(frames/1500)
            
        elif len(xcnts)>=40 and type=="right":
            dev_x.append(frames/1500)
            dev_yR.append(0)
    
    
        xcnts.clear()
        k = cv2.waitKey(1) & 0xff
        if k == ord('c'):
            break
    if type=="left":
        plt.plot(dev_x, dev_yL)
    elif type=="right":
        plt.plot(dev_x, dev_yR)


PROCESS(xyz)
#plt.plot(dev_x, dev_yL)
#plt.plot(dev_x, dev_yR)
plt.xlabel('Minutes since start')
plt.ylabel('Number of bees')
plt.show()
