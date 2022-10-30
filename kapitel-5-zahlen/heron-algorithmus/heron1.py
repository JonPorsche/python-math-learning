# 18_heron1.py
from math import fabs

A = 2.  # Flächeninhalt
eps = 1e-12  # Fehlergrenze
a = A  # Seite a des Rechtecks=Startwert
b = 1.  # Seite b des Rechtecks
print("\ta\t\t b\t\t\ta*b")
while fabs(a - b) > eps:
    print("%3.16f %3.16f %3.16f" % (a, b, a * b))
    a = (a + b) / 2  # Mittelwert bilden
    b = A / a  # Seitenverhältnis bilden
print(A ** (1 / 2), "genau")
