# 04_teiler.py
def berechne_teiler(zahl):
    teiler = []
    for t in range(2, zahl // 2 + 1):
        if zahl % t == 0:
            teiler.append(t)
        else:
            continue
    return teiler


# Hauptprogramm
z1 = int(input())
z2 = int(input())
print("Teiler von", z1, "=", berechne_teiler(z1))
print("Teiler von", z2, "=", berechne_teiler(z2))
