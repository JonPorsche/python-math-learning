# 22_eulersche_zahl.pi
from math import e

N = 10
for n in range(1, N):
    en = (1 + 1 / n) ** n
    print(en)
print(e, "genau")
