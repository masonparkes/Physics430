import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt
import scipy.special as sp

N=30;
L=2
h=L/N
g=9.8
x=np.arange(-h/2,L+(h),h)

#%% Make the A matrix
A=np.zeros((N+2,N+2))
for i in range(1,N+1):
    A[i][i]=-2*x[i]/(h**2)
    A[i][i-1]=x[i]/(h**2)-1/(2*h)
    A[i][i+1]=x[i]/(h**2)+1/(2*h)
A[0][0]=1/h
A[0][1]=-1/h
A[N+1][N+1]=1
#%% Make the B matrix
B=np.identity(N+2)
B[0][0]=1/2
B[0][1]=1/2
B[N-1][N-1]=0

vals,vecs=la.eig(A,B)

#%% Convert eigenvalues into frequencies
w=np.sqrt(-g*np.real(vals))
#w=-T*np.real(vals)/mu #w**2
# Sort the eigenvalues and eigenvectors
ind= np.argsort(w)
w=w[ind]
vecs=vecs[:,ind]

for i in range(4):
    plt.clf()
    plt.plot(vecs[:,i],x,'g^')
    plt.ylim(0,L)
    plt.xlim(-0.4, 0.4)
    plt.title(w[i])
    plt.xlabel('x')
    plt.draw()
    plt.pause(1)
    
wcalc=sp.jn_zeros(0,N+2)*np.sqrt(g/(4*L))
pcterror=(w-wcalc)/wcalc*100
print("my w\tw_calc\t%error")
for i in range(N+2):
    print(f'{w[i]:.3f}\t{wcalc[i]:.3f}\t{pcterror[i]:.3f}')
plt.clf()
plt.plot(range(N+2),pcterror)


