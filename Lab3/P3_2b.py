import matplotlib.pyplot as plt
import Lab3Funcs as l3f
import numpy as np

wplot=np.arange(400,1900,2)
maxamps=np.zeros(len(wplot))
T=127
L=1.2
mu=0.003
x,h=np.linspace(0,L,100,retstep=True)
f=l3f.force(x)

for n in range(len(wplot)):
    w=wplot[n]   
    g=l3f.steadySol(f,h,w,T,mu)    
#    plt.clf()
#    plt.plot(x,g)
#    plt.title('$\omega-{:d}$'.format(w))
#    plt.xlabel('x')
#    plt.ylim([-0.002, 0.002])
#    plt.draw()
#    plt.pause(0.001)
    maxamps[n]=np.copy(max(g))
#    print(max(abs(g)))
plt.plot(wplot,maxamps)
