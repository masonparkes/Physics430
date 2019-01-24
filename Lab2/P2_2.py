import numpy as np
import matplotlib.pyplot as plt


for N in [3000,300,30]:

    a=0
    b=2
    x,h=np.linspace(a,b,N,retstep=True)
    
    y=(16*np.sin(3*x)+np.cos(6-x)-np.cos(6+x)+np.cos(2+3*x)-np.cos(2-3*x))/(16*np.sin(6))
    
    A=np.zeros((N,N))
    b=np.sin(x)
    b[0]=0
    b[N-1]=1
    
    for i in range(1,N-1):
        A[i][i]=9-2/(h**2)
        A[i][i+1]=1/(h**2)
        A[i][i-1]=1/(h**2)     
    A[0][0]=1
    A[N-1][N-1]=1
    
    myY=np.linalg.solve(A,b)
    
    plt.plot(x,myY,'r.')
    
    plt.plot(x,y,'b')
    plt.show()
