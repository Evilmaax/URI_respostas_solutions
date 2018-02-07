N = int(input())
z, soma, maior, menor = 0, 0, 0, 0

while z < N:
    X, Y = input().split(' ')
    X, Y = int(X), int(Y)

    if X < Y:
        menor = X
        maior = Y
    else:
        menor = Y
        maior = X

    for c in range(menor+1, maior):
        if c % 2 != 0:
            soma += c

    print(soma)
    soma = 0
    z += 1
