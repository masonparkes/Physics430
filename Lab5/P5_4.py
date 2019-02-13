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
g=0.2

t=0.4*h/c
#t=h/c
#t=2*h/c


yold=np.zeros_like(y)
for i in range(1,N+1):
    yold[i]=-(g*t-2)/4*(4*t*vy[i]+2*g*t**2*vy[i]-4*y[i]-(2*c**2*t**2/h**2)*(y[i+1]-2*y[i]+y[i-1]))
yold[0]=-yold[1]
yold[-1]=-yold[-2]

ynew=np.zeros_like(y)
j=0
T=0
tmax=25
plt.figure(1)

step=tmax/(t*1)
amps=np.zeros(int(tmax/t)+1)

while T<tmax:
    j=j+1
    T=T+t
    
    for i in range(1,N+1):
        ynew[i]=(1/(2+g*t))*(4*y[i]-2*yold[i]+g*t*yold[i]+2*(c*t/h)**2*(y[i+1]-2*y[i]+y[i-1]))
    ynew[0]=-ynew[1]
    ynew[-1]=-ynew[-2]
    yold=np.copy(y)
    y=np.copy(ynew)
    amps[j]=abs(max(y))
    if (j+250)%500==0:
        plt.clf()
        plt.plot(x,y,'b-')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('time-{:1.3f}'.format(T))
        plt.ylim([-.002, 0.002])
        plt.xlim([0,L])
        plt.draw()
        plt.pause(0.1)
plt.clf()
m=np.linspace(0,tmax,int(tmax/t)+1)
plt.plot(m,amps)
plt.plot(m,0.00125*np.exp(-g*m/2),'r')
plt.title("Look at that!")