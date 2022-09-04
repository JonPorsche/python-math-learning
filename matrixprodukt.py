# 11_for_schleife6.py

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
b = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

m = len(a)  # Anzahl der Zeilen
c = [[0] * m for i in range(m)]  # Leere (m,m)-Liste erzeugen

for i in range(m):  # Zeilen
    for j in range(m):  # Spalten
        for k in range(m):  # Spalten A; Zeilen B
            c[i][j] = c[i][j] + a[i][k] * b[k][j]  # Produktsumme

# Ausgaben
print("Anzahl der Zeilen m = ", m)
print("Matrix A\n", a)
print("Matrix B\n", b)
print("Matrixprodukt C\n", c)
