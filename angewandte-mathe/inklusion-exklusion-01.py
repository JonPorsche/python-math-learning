def count(M1, M2, M3):
    r = len(M1) + len(M2) + len(M3) - len(M1 & M2) - len(M1 & M3) - len(M2 & M3) + len(M1 & M2 & M3)
    print(len(M1), "+", len(M2), "+", len(M3), "-", len(M1 & M2), "-", len(M1 & M3), "-", len(M2 & M3), "+", len(M1 & M2 & M3), " = ", r)


def load_set(M, modN):
    for k in range(0, 999):
        if k % modN == 0:
            M.add(k)


A = set()
B = set()
C = set()

load_set(A, 2)
load_set(C, 5)
load_set(B, 3)

print("|A| = \t\t\t", len(A))
print("|B| = \t\t\t", len(B))
print("|C| = \t\t\t", len(C))
print("|A & B| = \t\t", len(A & B))
print("|A & C| = \t\t", len(A & C))
print("|B & C| = \t\t", len(B & C))
print("|A & B & C| = \t", len(A & B & C))

count(A, B, C)
