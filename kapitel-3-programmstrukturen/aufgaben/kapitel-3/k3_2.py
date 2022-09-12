def fakultaet(n):
    i = 1
    f = 1
    while i <= n:
        f *= i
        i += 1
    return f


number = 9
print(fakultaet(number))
