
import matplotlib.pyplot
import numpy as np
import os

L = 1
x = np.arange(-7,7, 0.001)
p1 = L/2*np.exp(-L*np.abs(x**(1/2)))
L = 0.5
p2 = L/2*np.exp(-L*np.abs(x**(1/2)))
L = 2
p3 = L/2*np.exp(-L*np.abs(x**(1/2)))
fig, ax = matplotlib.pyplot.subplots()
fig.set_figheight(5)
fig.set_figwidth(7)
ax.plot(x, p1, 'k', label='lambda = 1')
ax.plot(x, p2, 'k--', label='lambda = 0.5')
ax.plot(x, p3, 'k:', label='lambda = 2')
ax.legend(loc='upper right', fontsize='large')

matplotlib.pyplot.xlabel('f', fontsize='large')
matplotlib.pyplot.ylabel('p(f)', fontsize='large')
matplotlib.pyplot.tight_layout()

matplotlib.pyplot.show()
