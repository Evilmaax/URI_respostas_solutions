P, R = input().split(" ")
P, R = int(P), int(R)

if P == 1 and R == 1:
    print("A")
elif P == 1 and R == 0:
    print("B")
else:
    print("C")