# 07_scipy1.py

from scipy.optimize import fsolve, newton


def f(x):
    return x ** 2 - 9


# Nullstelle berechnen
x01, x02 = fsolve(f, [5, -20])
# x01, x02 = newton(f, [5, -20])

# Ausgabe
print("Nullstellen:", x01, x02)
