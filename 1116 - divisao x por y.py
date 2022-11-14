N = int(input())

for x in range(N):
    X, Y = input().split(' ')
    X, Y = int(X), int(Y)
    if Y != 0:
        print(X/Y)
    else:
        print('divisao impossivel')