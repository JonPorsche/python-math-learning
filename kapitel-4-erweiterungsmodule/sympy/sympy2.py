# 06_sympy2.py

from sympy import symbols, expand, solve, diff, integrate

x = symbols('x')
f = (x - 1) * (x - 2) * (x - 3)

# Berechnung aus den Linearfaktoren des Polynoms, den Term p
p = expand(f)

# Berechnung der 1. Ableitung des Polynoms p
df = diff(p, x, 1)

# Berechnung der Stammfunktion F des Polynoms p
F = integrate(p, x)

# Berechnung der Nullstellen des Polynoms p
L = solve(p, x)

print("\nPolynom\t\t\tp(x) =", p)
print("1. Ableitung\tf'(x) = ", df)
print("Stammfunktion\tF(x) =", F)
print("Nullstellen\t\t", L)
