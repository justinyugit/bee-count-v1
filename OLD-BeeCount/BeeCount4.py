#960x720
from matplotlib import pyplot as plt
import numpy as np
import cv2
cap = cv2.VideoCapture('/home/justin/Downloads/vid.h264')
fgbg=cv2.bgsegm.createBackgroundSubtractorMOG()
xcnts = []
dev_x=[]
dev_y=[]
dev_yR=[]
dev_yL=[]
frames=0

def PROCESS(type):
    
    while(frames<2000):
        ret, frame = cap.read()
        if (type=="left"):
            roi=frame[300:700, 0:480]
        if (type=="right"):
            roi=frame[300:700, 480:960]
            
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
        if len(xcnts)<200:
            dev_x.append(frames/1500)
            dev_y.append(len(xcnts))
        else:
            print("too high")
    
    
    
        xcnts.clear()
        k = cv2.waitKey(1) & 0xff
        if k == ord('c'):
            plt.plot(dev_x, dev_y)
            
            plt.xlabel('Seconds since start')
            plt.ylabel('Number of bees')
            plt.show()
              #+ len(xcnts)/frames)
            break




###################################################

while(frames<2000):
    ret, frame = cap.read()
    roi=frame[300:700, 0:960]
    roiL=frame[300:700, 0:480]
    roiR=frame[300:700, 480:960]
    fgmask = fgbg.apply(roi)
    
    cv2.imshow('frame', fgmask)
    cv2.imshow('actual', frame)
    cnts = cv2.findContours(fgmask, cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[-2]
    s1=5
    s2=400
    for cnt in cnts:
        if s1<cv2.contourArea(cnt)<s2:
            xcnts.append(cnt)
            

    print(len(xcnts))
    frames=frames+1
    if len(xcnts)<200:
        dev_x.append(frames/1500)
        dev_y.append(len(xcnts))
    else:
        print("too high")
    
    
    
    xcnts.clear()
    k = cv2.waitKey(1) & 0xff
    if k == ord('c'):
        plt.plot(dev_x, dev_y)
        plt.xlabel('Seconds since start')
        plt.ylabel('Number of bees')
        plt.show()
              #+ len(xcnts)/frames)
        break

plt.plot(dev_x, dev_y)
plt.xlabel('Minutes since start')
plt.ylabel('Number of bees')
plt.show()
cap.release()
cv2.destroyAllWindows()

