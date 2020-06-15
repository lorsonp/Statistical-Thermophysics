import matplotlib.pyplot
import numpy as np
import sympy
import os


# b = np.arange(0 , 1000, .01)
b = np.logspace(0, 50, 7000)
C =  -((np.exp(14 *b) *(98+128 *np.exp(2 *b)+np.exp(16 *b)))/(1+np.exp(15 *b)* np.cosh(b))**2)
C = C/b**2*(1.380*10**(-23))
#
# A = np.logspace(-10, 30,1000)
# u = - 1/2*np.tanh(1/(A))
# U = -((np.exp(15/A) * (15*np.cosh(1/A) + np.sinh(1/A)))/(np.exp(15/A) * np.cosh(1/A) + 1))

# print(Cv)
fig, ax = matplotlib.pyplot.subplots()
fig.set_figheight(5)
fig.set_figwidth(7)
# ax.semilogx(T*(1.380*10**(-23)), U, 'k:', label='U')
ax.plot(1/b, C, 'k:', label='Cv')
# matplotlib.pyplot.text(0, 1040, 'Stiff Conditions', fontsize='large')
# matplotlib.pyplot.text(0, 725, 'Non-Stiff Conditions', fontsize='large')
ax.legend(loc='upper center', fontsize='large')
matplotlib.pyplot.xlabel('T*kb', fontsize='large')
matplotlib.pyplot.ylabel('Cv', fontsize='large')
# matplotlib.pyplot.xlim(left=10)
matplotlib.pyplot.tight_layout()
# matplotlib.pyplot.tick_params(
#     axis='x',          # changes apply to the x-axis
#     which='both',      # both major and minor ticks are affected
#     bottom=False,      # ticks along the bottom edge are off
#     top=False,         # ticks along the top edge are off
#     labelbottom=False) # labels along the bottom edge are off
# matplotlib.pyplot.tick_params(
    # axis='y',          # changes apply to the x-axis
    # which='both',      # both major and minor ticks are affected
    # bottom=False,      # ticks along the bottom edge are off
    # top=False,         # ticks along the top edge are off
    # labelleft=False) # labels along the bottom edge are off
# print(Cv)
# print()
matplotlib.pyplot.show()



# C1 = (np.exp(15* b)*(np.exp(15* b) *np.sinh(b) + 15* np.exp(15* b)* np.cosh(b))*(15* np.cosh(b) + np.sinh(b)))
# C2 = (np.exp(15* b)* np.cosh(b) + 1)**2
# C3 = (15* np.exp(15* b)*(15* np.cosh(b) + np.sinh(b)))
# C4 = (np.exp(15* b)* np.cosh(b) + 1)
# C5 = (np.exp(15* b)*(15* np.sinh(b) + np.cosh(b)))
# C6 = (np.exp(15* b)* np.cosh(b) + 1)
# # print( C1,C2,C3,C4,C5,C6)
