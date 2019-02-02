X = int(input())
Y = int(input())

total = 0

if X < Y:
    for z in range(X, Y+1):
        if z % 13 != 0:
            total += z
else:
    for z in range(Y, X+1):
        if z % 13 != 0:
            total += z

print(total)