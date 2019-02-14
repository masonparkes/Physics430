from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

# make 1D x and y arrays
Nx=30
a=-1
b=1
x, hx=np.linspace(a,b,Nx,retstep=True)
Ny=30
c=-1
d=1
y, hy=np.linspace(c,d,Ny,retstep=True)

#Make the 2D Meshgrid
X,Y=np.meshgrid(x,y)

# Evaluate a function on this grid
Z=X**2+Y**2

# Plot the function as a surface
fig=plt.figure(1)
ax=fig.gca(projection='3d')
surf=ax.plot_surface(X,Y,Z,cmap=cm.viridis)
fig.colorbar(surf)