# 10_eratosthenes.py
from math import sqrt, ceil


def sieb(n):
    """Sieb des Eratosthenes"""
    kmax = ceil(sqrt(n))
    prim = []
    gestrichen = [False] * n
    for i in range(2, kmax):
        if not gestrichen[i]:
            for j in range(i ** 2, n, i):
                gestrichen[j] = True
                # print(i, j)
    for i in range(2, n):
        if not gestrichen[i]:
            prim.append(i)
    return prim


# Hauptprogramm
N = 100
print(sieb(N))
