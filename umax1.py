from scipy.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import math

def u(c):
    return -c[0]*c[1]
w=10
cons = ({'type': 'eq', 'fun': lambda c: c[0]+c[1]-w})
opt = minimize(u, (1,1), constraints=cons)
#opt
#opt['x']
#-opt['fun']
print(opt)

def iu(u, c0):
    return u/c0
def c1(c0):
    return w-c0
np.set_printoptions(precision=5)
plt.style.use('fivethirtyeight')
mpl.rcParams['savefig.dpi']=300
mpl.rcParams['font.family']='serif'

c0 = np.linspace(1,w)

plt.figure(figsize=(10,6))
plt.plot(c0, c1(c0), label='budget constraint', lw=3.0)
plt.plot(c0, iu(15, c0), '--', label='$u=15$')
plt.plot(c0, iu(25, c0), label='$u=25$')
plt.plot(c0, iu(35, c0), '-.', label='$u=35$')
plt.plot(opt['x'][0], opt['x'][1], 'ro', label='$c=(5, 5)$')
plt.legend(loc=0)
plt.show()

kappa=10/11
def U(c):
    return -(math.log(c[0]) + kappa*math.log(c[1]))

opt1 = minimize(U, (1,1), constraints=cons)
print(opt1)

