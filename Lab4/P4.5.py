import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt
import scipy.special as sp

N=150;
start=-5
stop=5
h=(stop-start)/N
x=np.arange(start-h/2,stop+(h),h)

#%% Make the A matrix
A=np.zeros((N+2,N+2))
for i in range(1,N+1):
    A[i][i]=(1/2)*(x[i])**4+1/(h**2)
    A[i][i-1]=-1/(2*h**2)
    A[i][i+1]=-1/(2*h**2)
A[0][0]=1/2
A[0][1]=1/2
A[-1][-1]=1/2
A[-1][-2]=1/2
#%% Make the B matrix
B=np.identity(N+2)
B[0][0]=0
B[-1][-1]=0

vals,vecs=la.eig(A,B)

#%% Convert eigenvalues into frequencies
newvals=np.real(vals)
#w=-T*np.real(vals)/mu #w**2
# Sort the eigenvalues and eigenvectors
ind= np.argsort(newvals)
newvals=newvals[ind]
vecs=vecs[:,ind]

for i in [0,2,3,4,5]:
    plt.clf()
    plt.plot(x,vecs[:,i]**2,'g')
    
    plt.title(newvals[i])
    plt.xlabel('x')
    plt.draw()
    plt.pause(2)
