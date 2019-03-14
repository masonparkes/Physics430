import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt
import scipy.special as sp

N=400;
L=10
start=0
stop=L
x,h=np.linspace(start,stop,N,retstep=True)

rho=1+np.exp(-200*(x/L-1/2)**2)
v0=1
v=v0*np.ones_like(x)

plt.clf()
plt.plot(x,rho)

tau=.1


A=np.zeros((len(x),len(x)))
B=np.zeros_like(A)


#C1=(-tau*v0[i+1]/(4*h))
#C2=(-tau*v0[i-1]/*4*h))

for i in range(1,len(x)-1):
    A[i,i-1]=(-tau*v[i-1]/(4*h))
    A[i,i]=1
    A[i,i+1]=-(-tau*v[i+1]/(4*h))
    B[i,i-1]=-(-tau*v[i-1]/(4*h))
    B[i,i]=1
    B[i,i+1]=(-tau*v[i+1]/(4*h))
A[0,0]=1;

A[-1,-1]=1;
A[-1,-2]=-2
A[-1,-3]=1



t=0
tmax=10
plt.figure(1)
loop=0
step=5#int(tmax/(tau*50))
times=np.arange(t,tmax+tau,tau)
Xexp=np.zeros_like(times)
while t<tmax:
    t=t+tau
    loop=loop+1
    r=B@rho;
    r[0]=1
    r[-1]=0
        
    rho=la.solve(A,r)
    
    if loop%step==0:
        plt.clf()
        plt.plot(x,rho)
        #plt.plot(x,np.real(psi))
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('time-{:1.3f}'.format(t))
        plt.ylim([0, 2])
        plt.xlim([0,L])
        plt.draw()
        plt.pause(0.1)
