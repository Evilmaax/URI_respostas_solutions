X = int(input())

while X != 0:
    for x in range(1, X+1):
        if x < X:
            print('{} '.format(x), end='')
        else:
            print(X)
    X = int(input())
