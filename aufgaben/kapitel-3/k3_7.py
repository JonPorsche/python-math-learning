import numpy


def pythagoras(a, b):
    """
    Berechnet die Hypotenuse c, die Abschnitte q, p
    und die Höhe h eines rechtwinkligen Dreiecks.
    Parameter: Kathete a und b.
    """
    c = numpy.sqrt(a ** 2 + b ** 2)
    p = a ** 2 / c
    q = b ** 2 / c
    h = numpy.sqrt(p * q)
    return c, p, q, h


a = int(input("Kathete a:"))
b = int(input("Kathete b:"))

c, p, q, h = pythagoras(a, b)

print("\nHypotenuse c =\t", round(c, 2))
print("Abschnitt p =\t", round(p, 2))
print("Abschnitt q =\t", round(q, 2))
print("Höhe h =\t\t", round(h, 2), "\n")

print(pythagoras.__doc__)
