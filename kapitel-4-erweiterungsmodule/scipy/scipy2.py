# 08_sciphy2.py

from scipy.integrate import quad


def f(x):
    return x ** 2 + 10 * x - 100


# Nullstelle berechnen
A = quad(f, 7, 10)

print("Bestimmtes Integral:", A)
