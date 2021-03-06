import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sc
import math


for N in [30]:

    a=0
    b=5
    x,h=np.linspace(a,b,N,retstep=True)
    
   
    A=np.zeros((N,N))
    b=np.copy(x)
    b[0]=0
    b[N-1]=1
    
    for i in range(1,N-1):
        A[i][i]=1-2/(h**2)-1/(x[i]**2)
        A[i][i-1]=1/(h**2)-1/(2*h*x[i])
        A[i][i+1]=1/(h**2)+1/(2*h*x[i])     
    A[0][0]=1
    A[N-1][N-1]=1
    
    myY=np.linalg.solve(A,b)
    
    plt.plot(x,myY,'r.')
    
    y=-4*sc.jv(1,x)/sc.jv(1,5)+x
    
    plt.plot(x,y,'b')
    plt.show()
   
    
   