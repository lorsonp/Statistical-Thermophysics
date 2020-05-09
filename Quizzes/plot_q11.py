
import matplotlib.pyplot
import numpy as np
import os

L = 1
x = np.arange(0,20, 0.001)
p = L/2*np.exp(-L*abs(x))
fig, ax = matplotlib.pyplot.subplots()
fig.set_figheight(5)
fig.set_figwidth(7)
ax.plot(x, p, 'k:', label='Total entropy')
print('here')
# matplotlib.pyplot.text(0, 1040, 'Stiff Conditions', fontsize='large')
# matplotlib.pyplot.text(0, 725, 'Non-Stiff Conditions', fontsize='large')
# ax.legend(loc='upper center', fontsize='large')
matplotlib.pyplot.xlabel('x', fontsize='large')
matplotlib.pyplot.ylabel('p(x)', fontsize='large')
# matplotlib.pyplot.ylim(top=10)
matplotlib.pyplot.tight_layout()
# matplotlib.pyplot.tick_params(
#     axis='x',          # changes apply to the x-axis
#     which='both',      # both major and minor ticks are affected
#     bottom=False,      # ticks along the bottom edge are off
#     top=False,         # ticks along the top edge are off
#     labelbottom=False) # labels along the bottom edge are off
# matplotlib.pyplot.tick_params(
#     axis='y',          # changes apply to the x-axis
#     which='both',      # both major and minor ticks are affected
#     bottom=False,      # ticks along the bottom edge are off
#     top=False,         # ticks along the top edge are off
#     labelleft=False) # labels along the bottom edge are off
matplotlib.pyplot.show()
