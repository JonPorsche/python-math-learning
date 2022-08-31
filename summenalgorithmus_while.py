# 05_while_schleife2.py

n = 9
i = 0
s = 0

print("i\tL-Wert\tR-Wert")

while i < n:
    i += 1
    sr = s # R-Wert
    s += i
    print(i, s, sr, sep='\t')