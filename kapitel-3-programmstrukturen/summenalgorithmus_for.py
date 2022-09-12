# 07_for_schleife2.py
N = 12
# Summe der geraden Zahlen
su = 0
for n in range(1, N, 2):
    su = su + n
# Summe der ungeraden Zahlen
sg = 0
for n in range(2, N + 1, 2):
    sg = sg + n
# Ausgabe
print("Die Summe der ungeraden Zahlen von 1 bis", N, "ist", su)
print("Die Summe der geraden Zahlen von 2 bis", N, "ist", sg)
