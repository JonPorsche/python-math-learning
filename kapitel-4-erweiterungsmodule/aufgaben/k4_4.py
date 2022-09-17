from sympy import symbols, diff, integrate, sin, cos

a, x = symbols('a x')

y1 = sin(a * x)
y2 = cos(a * x)

# Erste Ableitung der Funktionen
dy1 = diff(y1, x, 1)
dy2 = diff(y2, x, 1)

# Stammfunktion
F1 = integrate(y1, x)
F2 = integrate(y2, x)

print("\n1. Ableitung von y1:\t", dy1)
print("1. Ableitung von y2:\t", dy2)
print("Stammfunktion von y1:\t", F1)
print("Stammfunktion von y2:\t", F2)
