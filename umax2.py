import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.5, 10, 50)
u = np.log(x)
u1 = 1/x
u2=-1/x**2

np.set_printoptions(precision=5)
plt.style.use('fivethirtyeight')
plt.figure(figsize=(10,6))
plt.plot(x, u, label='$u$')
plt.plot(x, u1, '--', label='$du/dx$')
plt.plot(x, u2, '-.', label='$d^2u/dx^2$')
plt.legend(loc=0)
plt.show()
