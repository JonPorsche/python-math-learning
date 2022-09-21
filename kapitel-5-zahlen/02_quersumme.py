# 02_quersumme.py

# Division mit Rest (klassiche Lösung)
def quersumme1(z):
    qs = 0
    while z != 0:
        qs = qs + z % 10
        z = z // 10  # Ganzzahldivision
    return qs


# typische Lösung mit Python
def quersumme2(z):
    str_zahl = str(z)
    qs = 0
    for ziffer in str_zahl:
        qs = qs + int(ziffer)
    return qs


# Hauptprogramm
zahl = 123456789

# q = quersumme1(zahl)
q = quersumme2(zahl)

print("\nDie Quersume von", zahl, "ist", q)
