import numpy as np
import matplotlib.pyplot as plt

tmax=10
tau=2.1

t=np.arange(0,tmax+tau,tau)

N=int(tmax/tau)

y=np.zeros_like(t)
y[0]=1

for n in range(N-1):
    y[n+1]=((1-tau)/(1+tau))*(y[n])

plt.clf()
plt.plot(t,y)
