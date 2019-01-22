import scipy.special as sc
import math


for N in [300]:

    a=0
    b=2
    x,h=np.linspace(a,b,N,retstep=True)
    
   
    A=np.zeros((N,N))
    b=np.copy(x)
    b[0]=0
    b[N-1]=0
    
    for i in range(1,N-1):
        A[i][i]=9-2/(h**2)
        A[i][i-1]=1/(h**2)
        A[i][i+1]=1/(h**2) 
        
    A[0][0]=1
    
    A[N-1][N-1]=1
    A[N-1][N-2]=-1
    
    myY=np.linalg.solve(A,b)
    
    plt.plot(x,myY,'r.')
    
    y=(x/9)-(np.sin(3*x)/(27*np.cos(6)))
    
    plt.plot(x,y,'b')
    plt.show()
    
    err=np.sqrt(np.mean((myY-y)**2))
    print(err)