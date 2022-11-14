N = int(input())

for x in range(1, N+1):
    X, Y = input().split(' ')
    X, Y = int(X), int(Y)
    if X % 2 != 0:
        soma, cont = X, 2
        for y in range(1, Y):
            soma += X+cont
            cont += 2
    else:
        soma, cont = X+1, 3
        for y in range(1, Y):
            soma += X+cont
            cont += 2
    print(soma)