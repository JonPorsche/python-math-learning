# L_03_05.py
print("x1\tx2\tx3\tUND\tODER")
for x1 in False, True:
    for x2 in False, True:
        for x3 in False, True:
            y1 = x1 and x2 and x3
            y2 = x1 or x2 or x3
            print(x1, x2, x3, y1, y2, sep='\t')
