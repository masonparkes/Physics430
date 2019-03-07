from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
# Make the grid
xmin = -2
xmax = 2
Nx = 30
x,hx = np.linspace(xmin,xmax,Nx,retstep = True)
hx2 = hx**2
ymin = 0
ymax = 2
Ny = 30
y,hy = np.linspace(ymin,ymax,Ny,retstep = True)
hy2 = hy**2
X,Y = np.meshgrid(y,x)
# Initialize potential
V = 0.5*np.ones_like(X)
# Enforce boundary conditions
V[:,0] = 0
V[:,-1] = 0
V[0,:] = 1
V[-1,:] = 1
# Allow possibility of charge distribution
rho = np.zeros_like(X)
# Iterate
denom = 2/hx2 + 2/hy2
fig = plt.figure(1)
ep=1
Vscale=1
w=1.6
passes=0
while ep/Vscale>(10**-4) and passes<1000:
    ep=0
    passes=passes+1
    for j in range(1,len(x)-1):
        for k in range(1,len(y)-1):
            V[j,k] = w*(( (V[j+1,k] + V[j-1,k])/hx2
                     +(V[j,k+1] + V[j,k-1])/hy2
                     +rho[j,k]) / denom)+(1-w)*V[j,k]
    err=V[1:-1,1:-1]-((V[2:,1:-1]+V[:-2,1:-1])/hx2+(V[1:-1,2:]+V[1:-1,:-2])/hy2+rho[1:-1,1:-1])/denom
    ep=np.max(np.abs(err))
     # make plots every few steps
    if passes % 10 == 0:
        plt.clf()
        ax = fig.gca(projection='3d')
        surf = ax.plot_surface(X,Y,V)
        ax.set_zlim(-0.5, 2)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.draw()
        plt.pause(0.1)
