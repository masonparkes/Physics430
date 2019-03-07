import numpy as np
x=1;
change=1
while change>0.00001:
    xnew=np.exp(-x)
    change=np.abs(xnew-x)
    x=xnew
    print(x)
print("starting the new thing")
x=1;
change=1
while change>0.00001:
    xnew=-np.log(x)
    change=np.abs(xnew-x)
    x=xnew
    print(x)
