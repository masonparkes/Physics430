from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

# make 1D x and y arrays
Nx=50
a=-5
b=5
x, hx=np.linspace(a,b,Nx,retstep=True)
Ny=50
c=-5
d=5
y, hy=np.linspace(c,d,Ny,retstep=True)


#Make the 2D Meshgrid
X,Y=np.meshgrid(x,y)

mu=0.3
sig=2

Zinitial=np.exp(-5*(X**2+Y**2))
Vinitial=np.zeros_like(X)


Z=np.copy(Zinitial)

Z[0,:]=0#this sets horizontal row
Z[-1,:]=0#this sets horizontal row
Z[:,-1]=0#this sets a vertical row
Z[:,0]=0#this sets a vertical row

#fig=plt.figure(1)
#plt.clf()
#ax=fig.gca(projection='3d')
#surf=ax.plot_surface(X,Y,Z)
#ax.set_zlim(-0.5,0.5)
#plt.xlabel('x')
#plt.ylabel('y')
#plt.draw()
#plt.title('Zinitial')
#plt.pause(1)
    
tfinal=10
c=np.sqrt(sig/mu)
tau=.717*hx/c
t=np.arange(0,tfinal,tau)
skip=10


Znew=np.zeros_like(Z)
Zold=np.zeros_like(Z)

Zold[1:-1,1:-1]=-tau*Vinitial[1:-1,1:-1]+Z[1:-1,1:-1]+(sig*tau**2/(2*mu))*((Z[2:,1:-1]-2*Z[1:-1,1:-1]+Z[0:-2,1:-1])/hx**2+(Z[1:-1,2:]-2*Z[1:-1,1:-1]+Z[1:-1,0:-2])/hy**2)

#plt.clf()
#ax=fig.gca(projection='3d')
#plt.title('Zold')
#surf=ax.plot_surface(X,Y,Zold)
#ax.set_zlim(-0.5,0.5)
#plt.xlabel('x')
#plt.ylabel('y')
#plt.draw()
#plt.pause(4)
fig=plt.figure(1)

middle=np.zeros_like(t)


for m in range(len(t)):
    
    middle[m]=Z[int(Nx/2),int(Ny/2)]
    
    Znew[1:-1,1:-1]=2*Z[1:-1,1:-1]-Zold[1:-1,1:-1]+(sig/mu)*(tau**2)*((Z[2:,1:-1]-2*Z[1:-1,1:-1]+Z[0:-2,1:-1])/hx**2+(Z[1:-1,2:]-2*Z[1:-1,1:-1]+Z[1:-1,0:-2])/hy**2)
    
    Znew[0,:]=0#this sets horizontal row
    Znew[-1,:]=0#this sets horizontal row
    Znew[:,-1]=0#this sets a vertical row
    Znew[:,0]=0#this sets a vertical row
    
    Zold=np.copy(Z)
    Z=np.copy(Znew)
    
    if m%skip==0:
        plt.clf()
        ax=fig.gca(projection='3d')
        surf=ax.plot_surface(X,Y,Z,cmap=cm.viridis)
        ax.set_zlim(-0.5,0.5)
        plt.title(t[m])
        plt.xlabel('x')
        plt.ylabel('y')
        plt.draw()        
        plt.pause(0.1)
        
plt.clf()
plt.plot(t,middle)
plt.title('middle plot')





