# 07_primtest_naiv

from math import sqrt, ceil


def istPrim(zahl):
    kmax = ceil(sqrt(zahl))
    for k in range(2, kmax):
        if zahl % k == 0:  # ohne Rest teilbar
            return zahl, False  # also keine Primzahl
    return zahl, True  # ist eine Primzahl


# Hauptprogramm
z = int(input("\nTeste ob folgende Zahl eine Primzahl ist:"))
print(istPrim(z))
