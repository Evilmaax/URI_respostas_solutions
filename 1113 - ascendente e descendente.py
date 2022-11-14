X, Y = input().split(' ')

X, Y = int(X), int(Y)

while X != Y:
    if X > Y:
        print('Decrescente')
        X, Y = input().split(' ')
        X, Y = int(X), int(Y)
    elif X < Y:
        print('Crescente')
        X, Y = input().split(' ')
        X, Y = int(X), int(Y)