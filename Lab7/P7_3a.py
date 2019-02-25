import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt
import scipy.special as sp

N=80;
L=3
D=2
start=0
stop=L
h=(stop-start)/N
x=np.arange(start-h/2,stop+(h),h) 

T=np.sin(np.pi*x/L)


#plt.plot(x,T)
#plt.pause(3)


#t=0.2*h/c
#C=.5034
C=1
tau=C*(h**2)/D
#t=2*h/c


A=np.identity(N+2)
B=np.identity(N+2)
for i in range(1,N+1):
    A[i,i-1]=-1
    A[i,i]=(2*h**2)/(tau*D)+2
    A[i,i+1]=-1
    B[i,i-1]=1
    B[i,i]=(2*h**2)/(tau*D)-2
    B[i,i+1]=1
A[0,0]=-0.5;
A[0,1]=0.5;
A[-1,-1]=-0.5;
A[-1,-2]=0.5

j=0
t=0
tmax=0.03
plt.figure(1)

step=1#int(tmax/(tau*50))

while t<tmax:
    j=j+1
    t=t+tau

    r=B@T;
    r[0]=0;
    r[-1]=0;
    
    T=la.solve(A,r)
    
    if j%step==0:
        plt.clf()
        plt.plot(x,T,'b*')
        a=np.pi/L
        exact=np.sin(a*x)*np.exp(-D*t*a**2)
        plt.plot(x,exact,'r-')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('time-{:1.3f}'.format(t))
        plt.ylim([0, 1])
        plt.xlim([-0.02,0.07])
        plt.draw()
        plt.pause(0.1)
plt.clf()
plt.plot(x,T,'b*')
a=np.pi/L
exact=np.sin(a*x)*np.exp(-D*t*a**2)
plt.plot(x,exact,'r-')
plt.xlabel('x')
plt.ylabel('y')
plt.title('time-{:1.3f}'.format(t))
plt.ylim([0, 1])
plt.xlim([0,L])
plt.draw()
plt.pause(0.1)