import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
import math

h1=0.1
x1=[-h1,0,h1]
y1=np.exp(x1)
fd1=(y1[2]-y1[1])/h1
cd1=(y1[2]-y1[0])/(2*h1)
scnd1=(y1[2]-2*y1[1]+y1[0])/(h1**2)

h2=0.01
x2=[-h2,0,h2]
y2=np.exp(x2)
fd2=(y2[2]-y2[1])/h2
cd2=(y2[2]-y2[0])/(2*h2)
scnd2=(y2[2]-2*y2[1]+y2[0])/(h2**2)

h3=0.001
x3=[-h3,0,h3]
y3=np.exp(x3)
fd3=(y3[2]-y3[1])/h3
cd3=(y3[2]-y3[0])/(2*h3)
scnd3=(y3[2]-2*y3[1]+y3[0])/(h3**2)

errfd1=fd1-1
errfd2=fd2-1
errfd3=fd3-1
errcd1=cd1-1
errcd2=cd2-1
errcd3=cd3-1