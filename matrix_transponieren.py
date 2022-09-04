# 10_for_schleife5.py

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
m = len(a)  # Anzahl der Zeilen
# Leere (m,m)-Liste erzeugen
c = [[0] * m for i in range(m)]
for i in range(m):  # Zeilen
    for j in range(m):  # Spalten
        c[j][i] = a[i][j]
# Ausgabe
print("Anzahl der Zeilen m = ", m)
for i in range(m):
    print(a[i])
print("Transponierte")
for i in range(m):
    print(c[i])
