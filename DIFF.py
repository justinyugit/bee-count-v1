# Calculates difference between left and right feeder bee counts
# Created November 2019
# Written by Justin Yu

import csv
from matplotlib import pyplot as plt
import sys
from scipy.ndimage.filters import gaussian_filter1d
import numpy as np
import os

#this argument is used to determine the name of the csv's
name=sys.argv[1]
csvPath = os.path.dirname(os.path.realpath(name))
csvPathL = csvPath + "left.csv"
csvPathR = csvPath + "right.csv"
print(csvPathL)

xframe=[]
yR=[]
yL=[]
yLFlat=[]
yRFlat=[]
yDIFF=[]


with open(csvPathL) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    for row in csv_reader:
        yL.append(row)
    for sublist in yL:
        for item in sublist:
            yLFlat.append(item)
    for i in range(len(yLFlat)):
        xframe.append(i/1500)
        

with open(csvPathR) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    for row in csv_reader:
        yR.append(row)
    for sublist in yR:
        for item in sublist:
            yRFlat.append(item)
    #for i in range(len(yRFlat)):
            #xframe.append(i/1500)
        
            

npL = np.asarray(yLFlat)
npR = np.asarray(yRFlat)
npDIFF = npR-npL



plt.plot(xframe,npDIFF)

plt.title('Difference: Right Minus Left')
plt.xlabel('Minutes since start')
plt.ylabel('Number of bees')
plt.show()

