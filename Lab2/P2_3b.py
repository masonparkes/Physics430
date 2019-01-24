import numpy as np
import math
import matplotlib.pyplot as plt

N=5000
a=0
b=5
x,h=np.linspace(a,b,N,retstep=True)
  
   
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
    
plt.plot(x,myY,'g')


    
    
plt.show()

xval=0
i=int(4.5/h)


error=np.abs(myY[i]-8.72062327763513)
print(f'error at x={x[i]:.2f} is {error:.4f}')
print(f'in fact, y(4.5)={myY[i]:.2f}')
