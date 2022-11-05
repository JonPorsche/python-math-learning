# 09_plot_grenzwert1.py
import numpy as np
import matplotlib.pyplot as plt

N = 17
eps = 0.5  # Epsilon-Umgebung
g = 5  # Grenzwert
n = np.linspace(1, N, N, endpoint=True)


# n = np.arange(1, N + 1, 1)


def a(n):
    return 5 * (1 - 1 / (2 ** n))


plt.title(r"$a_{n}=5\left(1-\frac{1}{2^{n}}\right)$")
# Zeichnen
plt.scatter(n, a(n), marker='+', color='r')
# Schranken
plt.hlines(g + eps, 0, N + 1)
plt.hlines(g - eps, 0, N + 1)
# Achsenbeschriftung
plt.xlabel('n')
plt.ylabel('$a_{n}$')
# Skalierung
plt.xlim(0, N + 1)
plt.ylim(0, 8)
plt.show()
