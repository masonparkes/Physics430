import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt
import scipy.special as sp

N=30;
L=3.2
h=L/N
k=16
x=np.arange(-h/2,L+(h),h)

mu0=0.003
T=50

mu=mu0*np.exp(x/L)

#%% Make the A matrix
A=np.zeros((N+2,N+2))
for i in range(1,N+1):
    A[i][i]=-2*(T/mu[i])/(h**2)
    A[i][i-1]=(T/mu[i])/(h**2)
    A[i][i+1]=(T/mu[i])/(h**2)
A[0][0]=1/2
A[0][1]=1/2
#Combine the BC into this one statement because that way the eventual eigenvalue doesn't effect it
A[-1][-1]=k/2+T/(h)
A[-1][-2]=k/2-T/(h)
#%% Make the B matrix
B=np.identity(N+2)
B[0][0]=0

B[-1][-1]=0#-k/(2)
#B[-1][-2]=-k/(2)

vals,vecs=la.eig(A,B)

#%% Convert eigenvalues into frequencies
w=np.sqrt(-np.real(vals))
# Sort the eigenvalues and eigenvectors
ind= np.argsort(w)
w=w[ind]
vecs=vecs[:,ind]

for i in range(3):
    plt.clf()
    plt.plot(x,vecs[:,i],'g^')
    #check boundary conditions
    #print((vecs[0,i]+vecs[1,i])/2)
    #print(T*(vecs[-1,i]-vecs[-2,i])/h)
    #print(k*(vecs[-1,i]+vecs[-2,i])/2)
    plt.ylim(-0.3,0.3)
    #plt.xlim(0,L)
    plt.title(w[i])
    plt.xlabel('x')
    plt.draw()
    plt.pause(2)
    
