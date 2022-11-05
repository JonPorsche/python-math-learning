# 10_sympy_grenzwert.py
from sympy import *

n = symbols('n')
an = (3 * n ** 2 - 5 * n + 7) / (-9 * n ** 2 + 6 * n - 3)
ga = limit(an, n, oo)
print("Grenzwert von %s ist %3.2f" % (an, ga))
