import numpy as np

def maxRange(v0,theta):
    R=(v0**2)* np.sin(2*theta)/9.8
    return R
def maxHeight(v0,theta):
    vy=v0*np.sin(theta)
    h=vy**2 /(2*9.8)
    return h