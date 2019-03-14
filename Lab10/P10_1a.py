import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt
import scipy.special as sp
N=400;
L=10
start=0
stop=L
h=(stop-start)/N
x=np.arange(start-h/2,stop+(h),h) 

rho0=1+np.exp(-200*(x/L-1/2)**2)
v0=1
v=v0*np.ones_like(x)
rho0[0]=2-rho0[1]
rho0[-1]=2-rho0[1]

plt.clf()
plt.plot(x,rho0)
plt.pause(1)

rho=rho0
rhonew=np.zeros_like(x)
tau=0.001
j=0
T=0
Tmax=30
plt.figure(1)
step=Tmax/(tau*1)
while T<Tmax:
    j=j+1
    T=T+tau    
    rhonew[1:-1]=-tau/(2*h)*(rho[2:]*v[2:]-rho[0:-2]*v[0:-2])+rho[1:-1]
    rhonew[0]=2-rhonew[1]
    rhonew[-1]=2-rhonew[-2]
    rho=np.copy(rhonew)
    if (j)%100==0:
        plt.clf()
        plt.plot(x,rho,'b-')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('time-{:1.3f}'.format(T))
        plt.ylim([0, 2])
        plt.xlim([0,L])
        plt.draw()
        plt.pause(0.1)
