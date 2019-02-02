X, Y = input().split(' ')
X, Y = int(X), int(Y)

while X != 0 and Y != 0:
    if Y > 0 and X > 0:
        print('primeiro')
        X, Y = input().split(' ')
        X, Y = int(X), int(Y)
    elif Y < 0 and X > 0:
        print('quarto')
        X, Y = input().split(' ')
        X, Y = int(X), int(Y)
    elif Y < 0 and X < 0:
        print('terceiro')
        X, Y = input().split(' ')
        X, Y = int(X), int(Y)
    elif Y > 0 and X < 0:
        print('segundo')
        X, Y = input().split(' ')
        X, Y = int(X), int(Y)