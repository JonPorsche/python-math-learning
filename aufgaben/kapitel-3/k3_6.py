for a in False, True:
    for b in False, True:
        x = not(a and b)
        y = not a or not b
        if x == y:
            print("Gesetz von De Morgan stimmt")
        else:
            print("Gesetz von De Morgan stimmt nicht")