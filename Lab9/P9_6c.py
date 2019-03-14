from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import random as r
# Make the grid
xmin = -2
xmax = 2
Nx = 100
x,hx = np.linspace(xmin,xmax,Nx,retstep = True)
hx2 = hx**2
ymin = -2
ymax = 2
Ny = 100
y,hy = np.linspace(ymin,ymax,Ny,retstep = True)
hy2 = hy**2
X,Y = np.meshgrid(x,y)
# Initialize potential
V = 0.5*np.ones_like(X)

Mask=np.ones_like(V)
#for j in range(int(Nx*6/10),int(Nx*6.2/10)):
#    for k in range(int(Ny*1/10),int(Ny*9/10)):
#        Mask[j,k]=0
#for j in range(int(Nx*1/10),int(Nx*3.6/10)):
#    for k in range(int(Ny*8/10),int(Ny*9/10)):
#        Mask[j,k]=0
r.seed()
for m in range(1,100):
    Mask[int(r.random()*Nx),int(r.random()*Ny)]=0

V0=1
# Enforce boundary conditions
V[:,0] = -V0
V[:,-1] = V0
V[0,:] = 0
V[-1,:] = 0
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
V = 0.25*np.ones_like(X)
# Enforce boundary conditions
V[:,0] = -V0
V[:,-1] = V0
V[0,:] = 0
V[-1,:] = 0
while ep/Vscale>(10**-4) and passes<200:
    ep=0
    passes=passes+1
    for j in range(1,len(x)-1):
        for k in range(1,len(y)-1):
            if Mask[j,k]:
                V[j,k] = w*(( (V[j+1,k] + V[j-1,k])/hx2
                     +(V[j,k+1] + V[j,k-1])/hy2
                     +rho[j,k]) / denom)+(1-w)*V[j,k]
    err=V[1:-1,1:-1]-((V[2:,1:-1]+V[:-2,1:-1])/hx2+(V[1:-1,2:]+V[1:-1,:-2])/hy2+rho[1:-1,1:-1])/denom
    ep=np.max(np.abs(err))
# make plots every few steps
    
print(passes)
plt.clf()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X,Y,V,cmap=cm.gist_rainbow)
plt.title(passes)
ax.set_zlim(-0.5, 2)
plt.xlabel('x')
plt.ylabel('y')
plt.draw()
plt.pause(0.1)
    