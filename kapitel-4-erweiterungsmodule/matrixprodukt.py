# 02_matrixprodukt.py
import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

# Matrizenmultiplikation mit Infix-Operator
C1 = A @ B
C2 = B @ A

# Ausgaben
print("\nMatrix A\n", A)
print("\nZugriff auf A[1,1] =", A[1, 1])
print("\nTransponierte von A\n", A.T)
print("\nMatrix B\n", B)
print("\nTransponierte von B\n", B.T)
print("\nMultiplikation A @ B\n", C1)
print("\nMultiplikation B @ A\n", C2)
print("\nMultiplikation (A @ B).T\n", (A @ B).T)
print("\nMultiplikation B.T @ A.T\n", B.T @ A.T)
