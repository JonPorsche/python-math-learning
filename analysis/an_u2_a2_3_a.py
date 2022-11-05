from sympy import *

n = symbols('n')
an = (n+1) / (n - 2)
ga = limit(an, n, oo)
print("Grenzwert von %s ist %3.2f" % (an, ga))
