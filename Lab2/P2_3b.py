import numpy as np
import math
import matplotlib.pyplot as plt

error=100
N=100
while error>0.001:
    
    N=N*2
    a=0
    b=5
    h=(b-a)/N
    x=np.arange(a,b,h)
      
       
    A=np.zeros((N,N))
    b=x**2
    b[0]=0
    b[N-1]=3
        
    for i in range(1,N-1):
        A[i][i]=math.exp(x[i])-2/(h**2)
        A[i][i-1]=1/(h**2)-np.sin(x[i])/(2*h)
        A[i][i+1]=1/(h**2)+np.sin(x[i])/(2*h)     
    A[0][0]=1
    A[N-1][N-1]=1
    
    myY=np.linalg.solve(A,b)
        
    plt.plot(x,myY,'r^')
    
    
        
        
    plt.show()
    
    xval=0
    i=0
    while x[i+1]<=4.5:
        i+=1
        
    
    error=np.abs(myY[i]-8.72062327763513)
    print(error)
