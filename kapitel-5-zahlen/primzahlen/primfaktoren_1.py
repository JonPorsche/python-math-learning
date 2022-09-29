# 11_primfaktoren1.py

from sympy import primefactors


def primfaktoren(n):
    f = []
    t = 2
    while t ** 2 <= n:
        if n % t == 0:
            f.append(t)
            n = n // t
        else:
            t += 1
    f.append(n)
    return f


z = int(input("Zahl:"))
print("Primfaktoren von", z, "sind:")
print(primfaktoren(z))
print(primefactors(z), "Sympy")
