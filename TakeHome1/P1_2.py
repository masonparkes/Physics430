import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt
import scipy.special as sp

N=30;
L=3.2
h=L/N
x=np.arange(-h,L+(2*h),h)

mu0=0.003
T=50
m=0.003

mu=mu0*np.exp(x/L)

#%% Make the A matrix
A=np.zeros((N+3,N+3))
for i in range(1,N+2):
    A[i][i]=-2*(T/mu[i])/(h**2)
    A[i][i-1]=(T/mu[i])/(h**2)
    A[i][i+1]=(T/mu[i])/(h**2)
A[0][0]=1/2
A[0][1]=1/2
A[-1][-1]=m/(h**2)-T/(2*h)
A[-1][-2]=-2*m/(h**2)
A[-1][-3]=m/h**2+T/(2*h)
#%% Make the B matrix
B=np.identity(N+3)
B[0][0]=0

B[-1][-1]=0#-T/(2*h)
#B[-1][-3]=T/(2*h)

vals,vecs=la.eig(A,B)

#%% Convert eigenvalues into frequencies
w=np.sqrt(-np.real(vals))
# Sort the eigenvalues and eigenvectors
ind= np.argsort(w)
w=w[ind]
vecs=vecs[:,ind]

for i in range(4):
    plt.clf()
    plt.plot(x,vecs[:,i],'g^')
    #check boundary conditions
    #print((vecs[0,i]+vecs[1,i])/2)
    print("second derivative:")
    print((vecs[-1,i]-2*vecs[-2,i]+vecs[-3,i])*(m/h**2))
    print("first derivative:")
    print((vecs[-1,i]-vecs[-3,i])*(-T/(2*h)))
    plt.ylim(-0.3,0.3)
    plt.xlim(0,L)
    plt.title(w[i])
    plt.xlabel('x')
    plt.draw()
    plt.pause(1)
    

