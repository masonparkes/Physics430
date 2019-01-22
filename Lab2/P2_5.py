#%%
"""P2.5a
You can't do the problem listed because you couldn't make the A matrix
because it's supposed to have Sin(yn) in it, so you aren't just multiplying
by some number, you'd have to take the sine of it, and you can't just do that
"""
#%%
#P2.5b
maxerr=1
passes=0
yguess=np.zeros_like(x)

while maxerr>0.0000001:
    passes+=1
    N=30
    a=0
    b=3
    x,h=np.linspace(a,b,N,retstep=True)
    
    A=np.zeros((N,N))
    b=np.ones_like(x)-np.sin(yguess)
    b[0]=0
    b[N-1]=0
    
    for i in range(1,N-1):
        A[i][i]=-2/(h**2)
        A[i][i-1]=1/(h**2)
        A[i][i+1]=1/(h**2) 
        
    A[0][0]=1
    
    A[N-1][N-1]=1
    
    myY=np.linalg.solve(A,b)
    
    
    err=A@myY-(1-np.sin(myY))
    maxerr= np.sqrt(np.mean(err[1:-2]**2))
    yguess=myY


plt.plot(x,myY,'b')
plt.show()
