# 06_ggT.py

# Euklidischer Algorithmus
def ggT1(a, b):
    """Euklidischer Algorithmus:Wechselwegnahme"""
    while a != b:
        if a > b:
            a = a - b
        elif b > a:
            b = b - a
    return a


# Variablentausch
def ggT2(a, b):
    while a != b:
        if a < b:
            a, b = b, a
        a = a - b
    return a


# Division mit Rest
def ggT3(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def alg_choice(nr):
    if nr not in [1, 2, 3]:
        print("\nWähle bitte zwischen die 3 Optionen!")
        nr_new = get_choice()
        alg_choice(nr_new)
    elif 1:
        result = ggT1(z1, z2)
        return print("Ergebnis =", result)
    elif 2:
        result = ggT2(z1, z2)
        return print("Ergebnis =", result)
    elif 3:
        result = ggT3(z1, z2)
        return print("Ergebnis =", result)


def get_choice():
    print("\nWähle ein Algorithmus\n")
    print("1 = Euklidischer Algorithmus: Wechselwegnahme\n"
          "2 - Variablentausch\n"
          "3 = Division mit Rest\n")
    choice = int(input("Option:"))
    return choice


# Hauptprogramm
print("\nggT berechnen\n")
z1 = int(input("Zahl 1:"))
z2 = int(input("Zahl 2:"))

alg_choice(get_choice())
