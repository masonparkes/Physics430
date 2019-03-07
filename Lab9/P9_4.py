import numpy as np
import matplotlib.pyplot as plt
k=0
minpasses=1000
ws=np.linspace(.6,.7,10000)
p=np.zeros_like(ws)
for w in ws:
    x=1;
    change=1
    passes=1
    while change>0.00001:
        passes=passes+1
        xnew=w*np.exp(-x)+(1-w)*x
        change=np.abs(xnew-x)
        x=xnew
        #print(x)
    #print(passes)
    if passes<minpasses:
        minpasses=passes
        minomega=w
    p[k]=passes
    k=k+1
plt.clf()
plt.plot(ws,p)
plt.xlabel("omega")
plt.ylabel("passes")

x=1;
change=1
passes=1
w=minomega
while change>0.00001:
    passes=passes+1
    xnew=w*np.exp(-x)+(1-w)*x
    change=np.abs(xnew-x)
    x=xnew
    print(x)
print(passes)
print(minomega)