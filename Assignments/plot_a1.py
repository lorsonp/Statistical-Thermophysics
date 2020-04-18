import matplotlib.pyplot
import numpy as np
import os

s0 = 10
x = np.arange(0, 1, 0.00001)
s = np.log(x - x**2)+10
fig, ax = matplotlib.pyplot.subplots()
fig.set_figheight(5)
fig.set_figwidth(7)
ax.plot(x, s, 'k:', label='Total entropy')
print('here')
# matplotlib.pyplot.text(0, 1040, 'Stiff Conditions', fontsize='large')
# matplotlib.pyplot.text(0, 725, 'Non-Stiff Conditions', fontsize='large')
ax.legend(loc='upper center', fontsize='large')
matplotlib.pyplot.xlabel('Internal Energy', fontsize='large')
matplotlib.pyplot.ylabel('Total Entropy', fontsize='large')
matplotlib.pyplot.ylim(top=10)
matplotlib.pyplot.tight_layout()
matplotlib.pyplot.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False) # labels along the bottom edge are off
matplotlib.pyplot.tick_params(
    axis='y',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelleft=False) # labels along the bottom edge are off
matplotlib.pyplot.show()
