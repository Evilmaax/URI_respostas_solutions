P1, C1, P2, C2 = input().split(" ")

esq = int(P1) * int(C1)
dir = int(P2) * int(C2)

if esq == dir:
    print(0)
elif esq > dir:
    print(-1)
else:
    print(1)