# 13_rsa1.py

p = 499  # Primzahl
q = 547  # Primzahl
n = p * q  # Modul
phi = (p - 1) * (q - 1)  # Euler-Funktion
k = 1
m1 = 2525  # m < n
m2 = m1 ** (1 + k * phi) % n  # Satz von Euler

print("Modul n =", n)
print("Anzahl der zu n teilerfremden Zahlen =", phi)
print("m1 =", m1)
print("m2 =", m2)
