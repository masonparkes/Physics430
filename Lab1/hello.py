
import numpy as np
#import scipy.special as sps

x=np.arange(0,10,0.05)
y=np.sin(5*x)

import matplotlib.pyplot as plt


nhalf=len(x)//2
plt.plot(x[0:nhalf],y[0:nhalf],'r*')
plt.plot(x[nhalf:],y[nhalf:],'g^')
plt.show()

plt.xkcd()
plt.plot(x,y,'r^')
plt.show()
