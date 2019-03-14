from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
# Make the grid
xmin = -2
xmax = 2
Nx = 100
hx=np.abs((xmin-xmax)/Nx)
x = np.arange(xmin-hx/2,xmax+hx,hx)
hx2 = hx**2
ymin = 0
ymax = 2
Ny = 100
hy=np.abs((ymin-ymax)/Ny)
y = np.arange(ymin-hy/2,ymax+hy,hy)
hy2 = hy**2
X,Y = np.meshgrid(x,y,indexing="ij")

# Allow possibility of charge distribution
rho = np.zeros_like(X)
# Iterate
denom = 2/hx2 + 2/hy2
fig = plt.figure(1)

Vscale=1
R=(hy2*np.cos(np.pi/Nx)+hx2*np.cos(np.pi/Ny))/(hx2+hy2)
w=2/(1+np.sqrt(1-R**2))


passes=0;
ep=1

V = .5*np.ones_like(X)
V0=1

# Enforce boundary conditions
V[:,0] = 0
V[:,-1] = 0
V[0,:] = -V0
V[-1,:] = V0
while ep/Vscale>(10**-4) and passes<1000:
    ep=0
    passes=passes+1
    for j in range(1,len(x)-1):
        for k in range(1,len(y)-1):
            V[j,k] = w*(( (V[j+1,k] + V[j-1,k])/hx2
                     +(V[j,k+1] + V[j,k-1])/hy2
                     +rho[j,k]) / denom)+(1-w)*V[j,k]                
    V[:,-1]=V[:,-2]
    V[0,:]=V[1,:]
    err=V[1:-1,1:-1]-((V[2:,1:-1]+V[:-2,1:-1])/hx2+(V[1:-1,2:]+V[1:-1,:-2])/hy2+rho[1:-1,1:-1])/denom
    ep=np.max(np.abs(err))
# make plots every few steps
#    if passes % 10 == 0:
#        plt.clf()
#        ax = fig.gca(projection='3d')
#        surf = ax.plot_surface(X,Y,V,cmap=cm.gist_rainbow)
#        ax.set_zlim(0, 1)
#        plt.title(passes)
#        plt.xlabel('x')
#        plt.ylabel('y')
#        plt.xlim(-2,2)
#        plt.ylim(0,2)
#        plt.draw()
#        plt.pause(0.1)
print(passes)
plt.clf()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X,Y,V,cmap=cm.gist_rainbow)
ax.set_zlim(0, 1)
plt.title(passes)
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-2,2)
plt.ylim(0,2)
plt.draw()
plt.pause(0.1)