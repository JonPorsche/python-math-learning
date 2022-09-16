# 05_sympy1.py

from sympy import symbols, Matrix

a11, a12, a21, a22 = symbols('a11,a12,a21,a22')
b11, b12, b21, b22 = symbols('b11,b12,b21,b22')

A = Matrix([[a11, a12],
            [a21, a22]])

B = Matrix([[b11, b12],
            [b21, b22]])

S = A + B
P = A * B

# Ausgabe
print("A:", A)
print("B:", B)
print("Summe = \n", S)
print("Matrixprodukt =\n", P)
