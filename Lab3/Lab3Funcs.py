#%% Defining Functions
import numpy as np
def force(x):
    N=np.size(x)
    b=np.zeros_like(x)
    for i in range(1,N-1):
        if(x[i]>=0.8 and x[i]<=1):
            b[i]=0.73
    return b
def steadySol(f,h,w,T,mu):
    N=np.size(f)
    A=np.zeros((N,N))
    for i in range(1,N-1):
        A[i][i]=-(2*T)/(h**2)+(mu * w**2)
        A[i][i-1]=T/(h**2)
        A[i][i+1]=T/(h**2)  
    A[0][0]=1
    A[N-1][N-1]=1
    return np.linalg.solve(A,-f)