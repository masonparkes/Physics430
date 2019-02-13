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

plt.plot(x,y)

T=127
mu=0.003
c=np.sqrt(T/mu)
g=20

tau=h/c


yold=np.zeros_like(y)
ynew=np.zeros_like(y)

j=0
T=0
Tmax=0.4
plt.figure(1)

step=Tmax/(tau*1)
w=1080

f=np.zeros_like(x)
for i in range(N+2):
    if(x[i]>0.8 and x[i]<1):
        f[i]=0.73
while T<Tmax:
    j=j+1
    T=T+tau
    
    for i in range(1,N+1):
        ynew[i]=1/(1/tau**2+g/(2*tau))*(f[i]*np.cos(w*T)/mu+(2*y[i]-yold[i])/tau**2+(g*yold[i]/(2*tau))+((c/h)**2)*(y[i+1]-2*y[i]+y[i-1]))
    ynew[0]=-ynew[1]
    ynew[-1]=-ynew[-2]
    yold=np.copy(y)
    y=np.copy(ynew)
    if (j)%100==0:
        plt.clf()
        plt.plot(x,y,'b-')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('time-{:1.3f}'.format(T))
        plt.ylim([-0.01, 0.01])
        plt.xlim([0,L])
        plt.draw()
        plt.pause(0.1)
