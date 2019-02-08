import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt
import scipy.special as sp

N=200;
L=1.2
start=0
stop=L
h=(stop-start)/N
x=np.arange(start-h/2,stop+(h),h) 

vy=np.zeros_like(x)
y=np.zeros_like(x)
y[0]=-y[1]
y[-1]=-y[-2]

plt.plot(x,y)

c=2
g=2000

t=0.4*h/c
#t=h/c
#t=2*h/c


yold=np.zeros_like(y)

ynew=np.zeros_like(y)
j=0
T=0
tmax=1.3785
plt.figure(1)

step=tmax/(t*1)
amps=np.zeros(int(tmax/t)+1)
w=400
mu=0.003

f=np.zeros_like(x)
for i in range(N+2):
    if(x[i]>0.8 and x[i]<1):
        f[i]=0.73
while T<tmax:
    j=j+1
    T=T+t
    
    for i in range(1,N+1):
        ynew[i]=1/(1/t+g/(2*t))*(f[i]*np.cos(w*T)/mu+(2*y[i]-yold[i])/t**2+(g/(2*t))*yold[i]+(c/h)**2*(y[i+1])-2*y[i]+y[i-1])
    ynew[0]=-ynew[1]
    ynew[-1]=-ynew[-2]
    yold=np.copy(y)
    y=np.copy(ynew)
    if (j)%50==0:
        plt.clf()
        plt.plot(x,y,'b-')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('time-{:1.3f}'.format(T))
        #plt.ylim([-1, 1])
        plt.xlim([0,L])
        plt.draw()
        plt.pause(0.1)
