X = int(input())
Y = int(input())

if X < Y:
    for z in range(X+1, Y):
        if z % 5 == 2 or z % 5 == 3:
            print(z)
else:
    for z in range(Y+1, X):
        if z % 5 == 2 or z % 5 == 3:
            print(z)