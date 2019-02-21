from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

# make 1D x and y arrays
Nx=300
a=0
b=2
x, hx=np.linspace(a,b,Nx,retstep=True)
Ny=300
c=-1
d=3
y, hy=np.linspace(c,d,Ny,retstep=True)

#Make the 2D Meshgrid
X,Y=np.meshgrid(x,y)

# Evaluate a function on this grid
Z=np.exp(-X**2-Y**2)*np.cos(5*np.sqrt(X**2+Y**2))

# Plot the function as a surface
fig=plt.figure(1)
plt.clf()
ax=fig.gca(projection='3d')
surf=ax.plot_surface(X,Y,Z,cmap=cm.viridis)
plt.ylabel('y')
plt.xlabel('x')
fig.colorbar(surf)