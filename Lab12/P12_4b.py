import matplotlib.pyplot as plt
import numpy as np
import scipy.linalg as la

# Physical constants
alpha = 0.01

# Make the grid
N = 500
L = 10
h = L/N
x = np.linspace(h/2,L-h/2,N)

# Initial Gaussian centered on the computing region
ymax = 2
y = ymax * np.exp(-(x-.5*L)**2)

# Time range
tau = 0.01
tfinal = 10
t = np.arange(0,tfinal,tau)

# Initialize the parts of the A and B matrices that
# do not depend on ybar and load them into At and Bt.
# Make them be sparse so the code will run fast.
At = np.zeros((N,N))
Bt = np.zeros((N,N))

# Function to wrap the column index
def jwrap(j):
    if (j < 0):
        return j + N
    if (j >= N):
        return j - N
    return j

# load the matrices with the terms that don't depend on ybar
h3 = h**3
for j in range(N):
    At[j,jwrap(j-1)] =-0.5*alpha/h3
    At[j,j]          = 0.5/tau + 1.5*alpha/h3
    At[j,jwrap(j+1)] = 0.5/tau - 1.5*alpha/h3
    At[j,jwrap(j+2)] = 0.5*alpha/h3

    Bt[j,jwrap(j-1)] = 0.5*alpha/h3
    Bt[j,j]          = 0.5/tau - 1.5*alpha/h3
    Bt[j,jwrap(j+1)] = 0.5/tau + 1.5*alpha/h3
    Bt[j,jwrap(j+2)] =-0.5*alpha/h3


plt.figure(1)
skip = 10
for n in range(len(t)):
    # Predictor step
    A = np.copy(At)
    B = np.copy(Bt)

    # load ybar, then add its terms to A and B
    ybar = np.copy(y)
    for j in range(N):
        tmp = 0.25*(ybar[jwrap(j+1)] + ybar[j])/h
        A[j,j]          = A[j,j] - tmp
        A[j,jwrap(j+1)] = A[j,jwrap(j+1)] + tmp
        B[j,j]          = B[j,j] + tmp
        B[j,jwrap(j+1)] = B[j,jwrap(j+1)] - tmp

    # do the predictor solve
    r = B@y
    yp = la.solve(A,r)

    # corrector step
    A = np.copy(At)
    B = np.copy(Bt)

    # average current and predicted y values to correct ybar
    ybar=.5*(y+yp)
    for j in range(N):
        tmp = 0.25*(ybar[jwrap(j+1)] + ybar[j])/h
        A[j,j]          = A[j,j] - tmp
        A[j,jwrap(j+1)] = A[j,jwrap(j+1)] + tmp
        B[j,j]          = B[j,j] + tmp
        B[j,jwrap(j+1)] = B[j,jwrap(j+1)] - tmp

    # do the final corrected solve
    r = B@y
    y = la.solve(A,r)

    if (n % skip == 0):
        plt.clf()
        plt.plot(x,y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('time={:1.3f}'.format(t[n]))
        plt.ylim(0,3)
        plt.pause(.1)
