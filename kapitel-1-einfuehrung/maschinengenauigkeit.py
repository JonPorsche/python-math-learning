# Berechnung der Maschinengenauigkeit
eps = 1.
while(1.0 + eps) != 1.0:
    eps = eps / 2.0
print(eps)
