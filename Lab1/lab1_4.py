import numpy as np
import scipy.special as sc
import matplotlib.pyplot as plt

N=20
a=0
b=5
x,h=np.linspace(a,b,N,retstep=True)
f=1*sc.jv(0,x)

fp=np.zeros_like(f)
fp[1:N-1]=(f[2:N]-f[0:N-2])/(2*h)
fp[0]=2*fp[1]-fp[2]
fp[N-1]=2*fp[N-2]-fp[N-3]

fpp=np.zeros_like(f)
fpp[1:N-1]=(f[2:N]-2*f[1:N-1]+f[0:N-2])/(h**2)
fpp[0]=2*fpp[1]-fpp[2]
fpp[N-1]=2*fpp[N-2]-fpp[N-3]

plt.plot(x,f,'b')
plt.plot(x,fp,'g')
plt.plot(x,fpp,'r')

plt.show()

plt.plot(x,fp,'g')
plt.plot(x,-sc.jv(1,x),'y^')
plt.plot(x,fpp,'b')
plt.plot(x,(1/2)*(-sc.jv(0,x)+sc.jv(2,x)),'r^')
plt.show()