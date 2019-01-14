# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 15:09:46 2019

@author: mrparkes
"""

import numpy as np
import matplotlib.pyplot as plt

N=100
a=0
b=np.pi
x,h=np.linspace(a,b,N,retstep=True)
plt.xkcd()
plt.plot(x,np.sin(x)*np.sinh(x))
plt.show()
print("there are {:d} gridpoints and cells in a cell edged grid".format(len(x)))

x2=np.arange(1/100,2,2/100)
y2=np.cos(x2)
plt.plot(x2,y2)
plt.show();
area=sum(y2)*2/100
print("Area under the curve is {:5.5f}".format(area))
print("Which compares pretty well to Sin(2)={:5.5f}".format(np.sin(2)))
area1=sum(np.cos(x))*h

step=b/1000
x3=np.arange(-step/2,b/2+step,step)
y3=np.sin(x3)
plt.plot(x3,y3,'y*')
plt.show()
print(y3[0])
print(y3[1])
