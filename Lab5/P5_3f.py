import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt
import scipy.special as sp

N=200;
L=1
start=0
stop=L
h=(stop-start)/N
x=np.arange(start-h/2,stop+(h),h) 

vy=0.01*np.exp(-(x-L/2)**2 / 0.02)
y=np.zeros_like(vy)
y[0]=-y[1]
y[-1]=-y[-2]

plt.plot(x,y)

c=2

t=0.4*h/c
#t=h/c
#t=2*h/c



for i in range(1,N+1):
    yold=y-vy*t+(y[i+1]-2*y[i]+y[i-1])*(c*t/h)**2
yold[0]=-yold[1]
yold[-1]=-yold[-2]

ynew=np.zeros_like(y)
j=0
T=0
tmax=2
plt.figure(1)

step=tmax/(t*100)

while T<tmax:
    j=j+1
    T=T+t
    
    for i in range(1,N+1):
        ynew[i]=2*y[i]-yold[i]+(y[i+1]-2*y[i]+y[i-1])*(c*t/h)**2
    ynew[0]=-ynew[1]
    ynew[-1]=-ynew[-2]
    yold=np.copy(y)
    y=np.copy(ynew)
    
    if j%step==0:
        plt.clf()
        plt.plot(x,y,'b-')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('time-{:1.3f}'.format(T))
        plt.ylim([-.002, 0.002])
        plt.xlim([0,L])
        plt.draw()
        plt.pause(0.1)