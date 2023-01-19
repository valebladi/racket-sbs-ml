import serial
import numpy as np
from keras.models import load_model
import matplotlib.pyplot as plt

model=load_model('modeldiscrete2.h5')
ser = serial.Serial('/dev/cu.HC-06-DevB',9600)             
data = open("data.txt","w")
max=1023
res1 = 560.0
res2 = 516.0
res3 = 516.0
res4 = 508.0
C1=1000000.0/res1
C2=1000000.0/res2
C3=1000000.0/res3
C4=1000000.0/res4
F1=(C1-1000)/30.0
F2=(C2-1000)/30.0
F3=(C3-1000)/30.0
F4=(C4-1000)/30.0
fsrVoltage1=0.0
fsrVoltage2=0.0
fsrVoltage3=0.0
fsrVoltage4=0.0
fsrR1=0.0
fsrR2=0.0
fsrR3=0.0
fsrR4=0.0
fsrC1=0.0
fsrC2=0.0
fsrC3=0.0
fsrC4=0.0
fsrF1=0.0
fsrF2=0.0
fsrF3=0.0
fsrF4=0.0
HitF1=0.0
HitF2=0.0
HitF3=0.0
HitF4=0.0

rn=1500.0
rn2=56000.0
rn3=150.0
m=0.058


while ser:
    b = ser.readline()
    c = b.split()
    if (c[0] != '0' and c[1] != '0' and c[2] != '0' and c[3] != '0'):
        print("\n")
        print (b)
        
        data.write(str(b) + "\n")
        c[0] = int(c[0])
        c[1] = int(c[1])
        c[2] = int(c[2])
        c[3] = int(c[3])
        
        a=c[0]/1023
        b=c[1]/1023
        xs=c[2]/1023
        d=c[3]/1023

        fsrVoltage1=4.8875*c[0]
        fsrVoltage2=4.8875*c[1]
        fsrVoltage3=4.8875*c[2]
        fsrVoltage4=4.8875*c[3]

        fsrVoltage1=fsrVoltage1/(rn2/(((rn*res1)/(rn+res1))+rn3))
        fsrVoltage2=fsrVoltage2/(rn2/(((rn*res2)/(rn+res2))+rn3))
        fsrVoltage3=fsrVoltage3/(rn2/(((rn*res3)/(rn+res3))+rn3))
        fsrVoltage4=fsrVoltage4/(rn2/(((rn*res4)/(rn+res4))+rn3))

        fsrR1=fsrVoltage1/((5000.0/1500)*(res1/(res1+rn)))
        fsrR2=fsrVoltage2/((5000.0/1500)*(res2/(res2+rn)))
        fsrR3=fsrVoltage3/((5000.0/1500)*(res3/(res2+rn)))
        fsrR4=fsrVoltage4/((5000.0/1500)*(res4/(res4+rn)))

        fsrR1=res1-fsrR1
        fsrR2=res2-fsrR2
        fsrR3=res3-fsrR3
        fsrR4=res4-fsrR4

        fsrC1=1000000.0/fsrR1
        fsrC2=1000000.0/fsrR2
        fsrC3=1000000.0/fsrR3
        fsrC4=1000000.0/fsrR4

        fsrF1=(fsrC1-1000.0)/30.0
        fsrF2=(fsrC2-1000.0)/30.0
        fsrF3=(fsrC3-1000.0)/30.0
        fsrF4=(fsrC4-1000.0)/30.0

        HitF1=fsrF1-F1
        HitF2=fsrF2-F2
        HitF3=fsrF3-F3
        HitF4=fsrF4-F4 

        acc1=HitF1/m
        acc2=HitF2/m
        acc3=HitF3/m
        acc4=HitF4/m

        print "Force TOP:",HitF1," N"
        print "Force BOTTOM:",HitF2," N"
        print "Force LEFT:",HitF3," N"
        print "Force RIGHT:",HitF4," N"

        print "Acceleration TOP:",acc1," m/s2"
        print "Acceleration BOTTOM:",acc2," m/s2"
        print "Acceleration LEFT:",acc3," m/s2"
        print "Acceleration RIGHT:",acc4," m/s2"

        test_input_data=np.array([[a,b,xs,d],[a,b,xs,d]])
        prediction = model.predict(test_input_data)
        maxval=np.argmax(prediction)
        prob1=prediction[0][maxval]
        prediction[0][maxval]=0
        prediction[1][maxval]=0
        maxval2=np.argmax(prediction)
        prob2=prediction[0][maxval2]

        x_y_coordinates = np.array([[10, 9], [17, 9], [8.5, 12], [13.5, 12], [18.5, 12], [8.5, 18.5], [13.5, 18.5], [18.5, 18.5], [8.5, 23], [13.5, 23], [18.5, 23], [9, 27], [18.5, 27]])
        x=x_y_coordinates[maxval][0]
        y=x_y_coordinates[maxval][1]
        x2=x_y_coordinates[maxval2][0]
        y2=x_y_coordinates[maxval2][1]
        print(x,y)
        print(prob1)
        print(x2,y2)
        print(prob2)
        height = 28
        width = 35
        rq = plt.imread("racket.png")
        plt.imshow(rq, extent=[0, height, 0, width])
        plt.scatter([x], [y],  c='y', s=1500)
        plt.savefig('pos.png')
        plt.clf()

        rq = plt.imread("racket.png")
        plt.imshow(rq, extent=[0, height, 0, width])
        plt.scatter([x2], [y2],  c='y', s=1500)
        plt.savefig('pos2.png')
        plt.clf()
        #plt.show()
        
ser.close()
data.close()

