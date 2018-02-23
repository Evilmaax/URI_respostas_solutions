X, soma, cont = 0, 0, 0

while X >= 0:
    X = int(input())
    if X > 0:
        soma += X
        cont += 1

print('{:.2f}' .format(soma/cont))