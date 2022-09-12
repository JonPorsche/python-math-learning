from math import *


def dreieck(a, b, c):
    """
    Berechnet der Umfang, die Flächeninhalt (Satz des Heron)
    und die Winkeln (Kosinussatz)
    :param a: Seite a des Dreiecks
    :param b: Seite b des Dreiecks
    :param c: Seite c des Dreiecks
    :return: Umfang, Flächeninhalt und Winkeln (alpha, beta, gamma)
    """
    U = a + b + c
    s = U / 2
    A = sqrt(s * ((s - a) * (s - b) * (s - c)))
    alpha = degrees(acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)))
    beta = degrees(acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c)))
    gamma = degrees(acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b)))
    return U, A, alpha, beta, gamma


a1 = 7
b1 = 4
c1 = 5

U, A, alpha, beta, gamma = dreieck(a1, b1, c1)

print("Umfang =\t\t", U)
print("Flächeninhalt:\t", A)
print("Winkel alpha =\t", alpha)
print("Winkel beta =\t", beta)
print("Winkel gamma =\t\n", gamma)
print(dreieck.__doc__)