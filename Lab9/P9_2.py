from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
# Make the grid
xmin = 0
xmax = 2
Nx = 80
x,hx = np.linspace(xmin,xmax,Nx,retstep = True)
hx2 = hx**2
ymin = 0
ymax = 2
Ny = 40
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
for n in range(200):
    for j in range(1,len(x)-1):
        for k in range(1,len(y)-1):
            V[j,k] = ( (V[j+1,k] + V[j-1,k])/hx2
                     +(V[j,k+1] + V[j,k-1])/hy2
                     +rho[j,k]) / denom
     # make plots every few steps
    if n % 10 == 0:
        plt.clf()
        ax = fig.gca(projection='3d')
        surf = ax.plot_surface(X,Y,V)
        ax.set_zlim(-0.5, 2)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.draw()
        plt.pause(0.1)