import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative

h = 1e-3 # Schrittweite
x1, x2 = 0, 4

# lokales Maximum (nach unten geöffnete Normalparabel)
def fmax(x):
    return -(x - 2) ** 2 + 5


def fmax_1(x):
    return derivative(fmax, x, dx=h)


def fmax_2(x):
    return derivative(fmax_1, x, dx=1)

# lokales Minimum (nach oben geöffnete Normalparabel)
def fmin(x):
    return (x - 2) ** 2


def fmin_1(x):
    return derivative(fmin, x, dx=h)


def fmin_2(x):
    return derivative(fmin_1, x, dx=1)


x = np.linspace(x1, x2, 500, endpoint=True)

# 3 Zeilen 2 Spalten
fig, ax = plt.subplots(3, 2, figsize=(8, 8))
# 1. Zeile, 1. Spalte
ax[0, 0].set_title("lokales Maximum")
ax[0, 0].plot(x, fmax(x), lw=2, color='r')
ax[0, 0].grid(True)
ax[0, 0].set_ylabel("y", rotation=True)
# 2. Zeile, 1. Spalte
ax[1, 0].set_title("1. Ableitung")
ax[1, 0].plot(x, fmax_1(x), lw=2, color='b')
ax[1, 0].plot(2, 0, 'ro')  # Nullstelle
ax[1, 0].grid(True)
ax[1, 0].set_ylabel("y", rotation=True)
# 3. Zeile, 1.Spalte
ax[2, 0].set_title("2. Ableitung")
ax[2, 0].plot(x, fmax_2(x), lw=2, color='g')
ax[2, 0].set_ylim(-3, 1)
ax[2, 0].grid(True)
ax[2, 0].set_xlabel("x")
ax[2, 0].set_ylabel("y", rotation=True)
# 1. Zeile, 2. Spalte
ax[0, 1].set_title("lokales Minimum")
ax[0, 1].plot(x, fmin(x), lw=2, color='r')
ax[0, 1].grid(True)
# 2. Zeile, 2. Spalte
ax[1, 1].set_title("1. Ableitung")
ax[1, 1].plot(x, fmin_1(x), lw=2, color='b')
ax[1, 1].plot(2, 0, 'ro')  # Nullstelle
ax[1, 1].grid(True)
# 3. Zeile, 2. Spalte
ax[2, 1].set_title("2. Ableitung")
ax[2, 1].plot(x, fmin_2(x), lw=2, color='g')
ax[2, 1].set_ylim(-1, 3)
ax[2, 1].grid(True)
ax[2, 1].set_xlabel("x")
plt.tight_layout()
plt.show()
