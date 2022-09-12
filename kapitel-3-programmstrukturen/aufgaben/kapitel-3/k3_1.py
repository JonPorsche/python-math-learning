def multiply(a, b):
    return a * b


def add(a, b):
    return a + b


def divide(a, b):
    return a / b


def calc(a, b):
    if (a + b) == 0:
        return print("Nenner darf nicht gleich 0 sein!")
    else:
        c = divide(multiply(a, b), add(a, b))
        print("Ergebnis = ", c)

a = float(input("a: "))
b = float(input("b: "))
calc(a, b)

