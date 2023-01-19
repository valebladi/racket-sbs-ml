import matplotlib.pyplot as plt
import numpy as np

'''
rq = plt.imread("racket.png")
bl = plt.imread("ball.png")

x=10
y=15

height = 22
width = 25

a = np.zeros((height,width))

for i in range(0,height):
    for j in range(0,width):
        if i == x and j == y:
            a[j,i] = 0.5


#fig, ax = plt.subplots()
#x = range(10)
plt.imshow(rq, extent=[0, height, 0, width])
#plt.plot(a)
#plt.imshow(a, cmap='hot', interpolation='nearest')

#ax.plot(x, x, '--', linewidth=5, color='firebrick')

plt.scatter([10], [20],  c='y', s=70)
plt.show()
plt.show()

'''

rq = plt.imread("racket.png")
num = 1
x=5
y=15
height = 20
width = 25
im = plt.imshow(rq, extent=[0, height, 0, width])
plt.scatter([10], [20],  c='y', s=1500)
plt.savefig(str(num)+'.png')
num= 2
x=5
y=15
height = 20
width = 25
im = plt.imshow(rq, extent=[0, height, 0, width])
plt.scatter([10], [20],  c='y', s=1500)
plt.savefig(str(num)+'.png')