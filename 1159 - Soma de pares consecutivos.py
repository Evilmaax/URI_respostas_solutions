X = int(input())

while X != 0:
    if X % 2 == 0:
        soma, cont = X, 2
        for z in range(1, 5):
            soma += X + cont
            cont += 2
    else:
        soma, cont = X+1, 3
        for z in range(1, 5):
            soma += X + cont
            cont += 2
    print(soma)
    X = int(input())