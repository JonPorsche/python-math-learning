# 10_sympy_konvergenzkriterien.py
from sympy import *

n = symbols('n')


def a(k):
    # return 4 * (-1) ** (k + 1) / (2 * k - 1)  # Kreiszahl π
    # return 1 / k  # harmonische Folge
    # return 1 / factorial(k - 1)  # eulersche Zahl e
    # return k**2/2**k            #Grenzwert 6
    # return k**3/3**k
    # return (k + 1 / k ** 2 + 3 * k) ** 2
    # return k / 2 ** k
    # return 2 ** k / factorial(k)
    # return 3 ** k / k ** k
    # return k ** 5 / factorial(k)
    return k ** 2 / (1 - k ** 2)


QK = limit(abs(a(n + 1) / a(n)), n, oo)  # <1
WK = limit(Pow(abs(a(n)), 1 / n), n, oo)  # <1
g = limit(a(n), n, oo)

# Ausgabe
print("Quotientenkriterium:", QK)
print("Wurzelkriterium....:", WK)
print("Grenzwert.......:", g)
