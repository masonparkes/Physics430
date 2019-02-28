import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt
import scipy.special as sp

N=80;
L=3
D=20
start=0
stop=L
h=(stop-start)/N
x=np.arange(start-h/2,stop+(h),h) 

T0=np.sin(np.pi*x/L)
T0[0]=-T0[1]
T0[-1]=-T0[-2]

plt.title("initial thing")
plt.plot(x,T0)
plt.pause(0.1)


#t=0.2*h/c
#C=.5034
C=.5
tau=C*(h**2)/D
#t=2*h/c


T=np.zeros_like(T0)
j=0
t=0
tmax=1
plt.figure(1)

step=int(tmax/(tau*50))

while t<tmax:
    j=j+1
    t=t+tau
    
    T[1:-1]=T0[1:-1]+D*tau/(h**2)*(T0[2:]-2*T0[1:-1]+T0[0:-2])
    T[0]=-T[1]
    T[-1]=-T[-2]
    T0=np.copy(T)
    T=np.copy(T0)
    #print("here")
    if j%step==0:
        plt.clf()
        a=np.pi/L
        exact=np.sin(a*x)*np.exp(-D*t*a**2)
        plt.plot(x,exact,'r-')
        error=np.sqrt(np.mean((T-exact)**2))
        print(error)
        plt.plot(x,T,'b*')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('time-{:1.3f}'.format(t))
        plt.ylim([0, 1])
        plt.xlim([0,L])
        plt.draw()
        plt.pause(0.1)