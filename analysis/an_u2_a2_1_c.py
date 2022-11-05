from sympy import *

n = symbols('n')
an = 3 ** (1 / n) * (1 + 1 / n) ** n
ga = limit(an, n, oo)
print("Grenzwert von %s ist %3.2f" % (an, ga))
