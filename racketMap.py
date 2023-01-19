import matplotlib.pyplot as plt
import numpy as np
import serial
import time

rq = plt.imread("racket.png")
ser = serial.Serial('/dev/cu.usbserial-1420',9600)                   
data = open("data.txt","w")

#size of racket
height = 20
width = 25

while ser:
    b = ser.readline()
    c = b.split()
    if c[0] != '0' and c[1] != '0' and c[2] != '0' and c[3] != '0':
        print b
        data.write(str(b) + "\n")
        
        #Machine learning estimating the prosition in X and Y
        x = 5
        y = 10
        
        plt.imshow(rq, extent=[0, height, 0, width])
        plt.scatter([x], [y],  c='y', s=1200)
        plt.show()
        plt.pause(1) # <-------
        raw_input("<Hit Enter To Close>")
        plt.close()
ser.close()
data.close()
