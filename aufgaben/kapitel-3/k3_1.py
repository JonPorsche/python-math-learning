def multiply(a, b):
    return a * b


def add(a, b):
    return a + b


def divide(a, b):
    return a / b


def calc(a, b):
    if b == 0:
        return print("Nenner darf nicht gleich 0 sein!")
    return divide(multiply(a, b), add(a, b))

a = 4
b = 98.98
c = calc(a, b)

print("Ergebnis = ", c)
