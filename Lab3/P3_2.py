#%% Import necessary things
import numpy as np

#%% Defining constants
mu=0.003
N=100
T=127
L=1.2
w=400

#%% Set up matrices
x,h=np.linspace(0,L,N,retstep=True)
b=np.zeros_like(x)
A=np.zeros((N,N))
for i in range(1,N-1):
    A[i][i]=-(2*T)/(h**2)+(mu * w**2)
    A[i][i-1]=T/(h**2)
    A[i][i+1]=T/(h**2)
    if (x[i]>=0.8 and x[i]<=1):
        b[i]=0.73
A[0][0]=1
A[N-1][N-1]=1

#%% Solve for g(x)
g=np.linalg.solve(A,-b)

#%% Plot g as an xkcd graph :)
plt.xkcd()
plt.plot(x,g)


