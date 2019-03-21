import Lab11Funcs as S
import matplotlib.pyplot as plt
import numpy as np


# System Parameters
L = 10.0        # Length of tube
T0 = 293.       # Ambient temperature
rho0 = 1.3      # static density (sea level)

# speed of sound
c = np.sqrt(S.gamma * S.kB * T0 / S.M)

# cell-center grid with ghost points
N = 100
h = L/N
x = np.linspace(-.5*h,L+.5*h,N+2)

# initial distributions
rho = rho0 * np.ones_like(x)
T = T0 * np.ones_like(x)
v = np.exp(-200*(x/L-0.5)**2) * c/100

tau = 0.000046/h#0.0046*h#0.0001#0.000467
tfinal = 0.1
t = np.arange(0,tfinal,tau)
position=np.zeros_like(t)
skip = 50  #input(' Steps to skip between plots - ')

for n in range(len(t)):

    # Plot the current values before stepping
    if n % skip == 0:
        plt.clf()
        plt.subplot(3,1,1)
        plt.plot(x,rho)
        plt.ylabel('rho')
        plt.ylim(1.28, 1.32)
        plt.title('time={:1.3f}'.format(t[n]))
        plt.subplot(3,1,2)
        plt.plot(x,T)
        plt.ylabel('T')
        plt.ylim(292,294)
        plt.subplot(3,1,3)
        plt.plot(x,v)
        plt.ylabel('v')
        plt.ylim(-4,4)
        plt.xlabel('x')
        plt.pause(0.1)

    # 1. Predictor step for rho
    rhop = S.Srho(rho,v,v,tau,h)

    # 2. Predictor step for T
    Tp = S.ST(T,v,v,rho,rhop,tau,h)

    # 3. Predictor step for v
    vp = S.Sv(v,v,v,rho,rhop,T,Tp,tau,h)

    # 4. Corrector step for rho
    rhop = S.Srho(rho,v,vp,tau,h)

    # 5. Corrector step for T
    Tp = S.ST(T,v,vp,rho,rhop,tau,h)

    # 6. Corrector step for v
    v = S.Sv(v,v,vp,rho,rhop,T,Tp,tau,h)

    # Now put rho and T at the same time-level as v
    rho = rhop
    T = Tp
    position[n]=x[np.argmin(rho)]
plt.clf()
plt.subplot(3,1,1)
plt.plot(x,rho)
plt.ylabel('rho')
plt.ylim(1.28, 1.32)
plt.title('time={:1.3f}'.format(t[n]))
plt.subplot(3,1,2)
plt.plot(x,T)
plt.ylabel('T')
plt.ylim(292,294)
plt.subplot(3,1,3)
plt.plot(x,v)
plt.ylabel('v')
plt.ylim(-4,4)
plt.xlabel('x')
plt.pause(0.1)
print(np.mean(np.abs(np.diff(position)/tau)))
