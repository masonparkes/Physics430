import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt
import scipy.special as sp

N=200;
L=10
start=-2*L
stop=3*L

hbar=1;
m=1
sig=2;
p=-2*np.pi;

h=(stop-start)/N
x,h=np.linspace(start,stop,N,retstep=True) 

a=np.imag(0+1j)

psi=1/np.sqrt(sig*np.sqrt(np.pi))*np.exp(1j*p*x/hbar)*np.exp(-x**2/(2*sig**2))#guassian nonsense

plt.clf()



tau=.1

E=p**2/(2*m)+hbar**2/(4*m*sig**2)


A=np.zeros((N,N),dtype=np.complex)
B=np.zeros((N,N),dtype=np.complex)
V=np.zeros_like(x)
V0=E*.1
done=False
n=0
while True:
    n=n+1
    if x[n]>=0.5*L:
        n1=n
        break
while True:
    n=n+1
    if x[n]>=L:
        n2=n
        break
V[n1:n2]=V0


for i in range(1,N-1):
    A[i,i-1]=(hbar**2)/(4*m*h**2)
    A[i,i]=-(2*hbar**2)/(4*m*h**2)-V[i]/2+hbar*1j/tau
    A[i,i+1]=(hbar**2)/(4*m*h**2)
    B[i,i-1]=-(hbar**2)/(4*m*h**2)
    B[i,i]=(2*hbar**2)/(4*m*h**2)+V[i]/2+hbar*1j/tau
    B[i,i+1]=-(hbar**2)/(4*m*h**2)
A[0,0]=1;
A[-1,-1]=1;

t=0
tmax=50
plt.figure(1)
loop=0
step=5#int(tmax/(tau*50))
times=np.arange(t,tmax+tau,tau)
Xexp=np.zeros_like(times)
rightside=np.zeros_like(times)
leftside=np.zeros_like(times)
barrier=np.zeros_like(times)
total=np.zeros_like(times)
while t<tmax:
    t=t+tau
    Xexp[loop]=np.trapz(np.conjugate(psi)*x*psi*h)
    rightside[loop]=np.trapz(np.abs(np.conjugate(psi[0:n1])*psi[0:n1])*h)
    leftside[loop]=np.trapz(np.abs(np.conjugate(psi[n2:])*psi[n2:])*h)
    barrier[loop]=np.trapz(np.abs(np.conjugate(psi[n1:n2])*psi[n1:n2])*h)
    total[loop]=np.trapz(np.abs(np.conjugate(psi)*psi)*h)
    loop=loop+1
    r=B@psi;
    r[0]=0;
    r[-1]=0;
    
    psi=la.solve(A,r)
    
    if loop%step==0:
        plt.clf()
        plt.plot(x,np.abs(np.conjugate(psi)*psi))
        #plt.plot(x,np.real(psi))
        plt.plot(x,V/V0)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('time-{:1.3f}'.format(t))
        #plt.ylim([0, 1])
        plt.xlim([-2*L,3*L])
        plt.draw()
        plt.pause(0.1)
        #print("Right:")
        #print(np.trapz(np.abs(np.conjugate(psi[0:n1])*psi[0:n1])*h))
        #print("Left:")
        #print(np.trapz(np.abs(np.conjugate(psi[n2:])*psi[n2:])*h))
plt.clf()

plt.plot(times,total)
plt.plot(times,rightside,'r^')
plt.plot(times,leftside,'g^')
plt.plot(times,barrier,'b^')

plt.legend(["total prob","prob right","prob left","prob barrier"])
plt.title('<x>')