import numpy as np
from scipy.optimize import minimize

B = (10, (11, 11))
S = (10, (20, 5))
M0 = np.array((B[0], S[0]))
M = np.array((B[1], S[1])).T
p = 0.5
P = np.array((p, 1-p))
def U(phi):
    c1 = np.dot(M, phi)
    return -np.dot(P, np.log(c1))
w = 10
cons = ({'type': 'eq',
         'fun': lambda phi: np.dot(M0, phi) - w})
opt = minimize(U, (1, 1), constraints=cons)
print(opt)
print(np.dot(M, opt['x']))

M0 = np.array((1, B[0], S[0]))
kappa = 10/11
def U(phi):
    c0 = phi[0]
    c1 = np.dot(M, phi[1:])
    return -(np.log(c0) + kappa * np.dot(P, np.log(c1)))
opt = minimize(U, (1, 1, 1), constraints=cons)
print(opt)
print(np.dot(M, opt['x'][1:]))
