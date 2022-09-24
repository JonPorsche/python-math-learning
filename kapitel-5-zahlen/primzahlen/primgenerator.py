# 09_primgenerator.py

from sympy import sqrt, primerange


def primzahl(us, os):
    prim_zahlen = []
    ist_prim = False
    n = 0
    for zahl in range(us, os):
        ist_prim = True
        kmax = int(sqrt(zahl)) + 1  # größter Teiler
        for k in range(2, kmax):
            if zahl % k == 0:  # ohne Rest teilbar
                ist_prim = False  # keine Primzahl
                break
        if ist_prim:
            n = n + 1  # zähle Primzahlen
            prim_zahlen.append(zahl)
    return prim_zahlen, n


# Hauptprogramm
u = int(input("Untere Schranke:"))
o = int(input("Obere Schranke:"))
pz = primzahl(u, o)
pz_sympy = [i for i in primerange(u, o)]
print(pz)
print("", pz_sympy, len(pz_sympy))
