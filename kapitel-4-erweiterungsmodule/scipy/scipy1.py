# 07_scipy1.py

from scipy.optimize import fsolve, newton


def f(x):
    return x ** 2 + 10 * x - 100


# Nullstelle berechnen
x01, x02 = fsolve(f, [5, -20])
# x01, x02 = newton(f, [5, -20])

# Ausgabe
print("Nullstellen:", x01, x02)
