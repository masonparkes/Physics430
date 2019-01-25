import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt

N=30;
mu=0.003
T=127
L=1.2
x,h=np.linspace(0,L,N,retstep=True)


#%% Make the A matrix
A=np.zeros((N,N))
for i in range(1,N-1):
    A[i][i]=-2/(h**2)
    A[i][i-1]=1/(h**2)
    A[i][i+1]=1/(h**2)
A[0][0]=1
A[N-1][N-1]=1
#%% Make the B matrix
B=np.identity(N)
B[0][0]=0
B[N-1][N-1]=0
#%% Solve the eigenvalue problem
vals,vecs=la.eig(A,B)

#%% Convert eigenvalues into frequencies
w=np.sqrt(-T*np.real(vals)/mu)
# Sort the eigenvalues and eigenvectors
ind= np.argsort(w)
w=w[ind]
vecs=vecs[:,ind]

for i in range(4):
    plt.clf()
    plt.plot(x,vecs[:,i],'g^')
    amp=max(abs(vecs[:,i]))
    plt.plot(x,amp*np.sin((i+1)*np.pi*x/L),'y')
    plt.title(w[i])
    plt.xlabel('x')
    #plt.ylim([-0.002, 0.002])
    plt.draw()
    plt.pause(1)
plt.clf()
plt.xkcd()
plt.plot(x,vecs[:,20],'r*')
plt.plot(x,max(abs(vecs[:,20]))*np.sin(21*np.pi*x/L),'b')