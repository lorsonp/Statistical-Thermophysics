
import matplotlib.pyplot
import numpy as np
import os

L = 1
x = np.arange(0,20, 0.001)
p = L/2*np.exp(-L*x**2)
fig, ax = matplotlib.pyplot.subplots()
fig.set_figheight(5)
fig.set_figwidth(7)
ax.plot(x, p, 'k:', label='Total entropy')
print('here')

matplotlib.pyplot.xlabel('x', fontsize='large')
matplotlib.pyplot.ylabel('p_F(x)', fontsize='large')
matplotlib.pyplot.tight_layout()

matplotlib.pyplot.show()
