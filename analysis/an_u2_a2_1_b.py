from sympy import *

n = symbols('n')
an = (2 * n ** 2 + 3 * n) / (4 * n ** 2 + 1)
ga = limit(an, n, oo)
print("Grenzwert von %s ist %3.2f" % (an, ga))
