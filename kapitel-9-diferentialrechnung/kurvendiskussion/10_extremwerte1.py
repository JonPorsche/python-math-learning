import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative

h = 1e-6  # Schrittweite
x1, x2 = -5, 5
y1, y2 = -10, 4
plt.xlim(x1, x2)
plt.ylim(y1, y2)


def f(x):
    return -x ** 3 / 4 + 3 * x - 4


def df_1(x):
    return derivative(f, x, dx=h)


def df_2(x):
    return derivative(df_1, x, dx=h)


x = np.linspace(x1, x2, 500)
plt.plot(x, f(x), lw=2, color='r')
plt.plot(x, df_1(x), 'b--', label='1. Ableitung')
plt.plot(x, df_2(x), 'g--', label='2. Ableitung')
plt.legend(loc='best')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
