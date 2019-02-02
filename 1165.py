N = int(input())

for y in range(0, N):
    X = int(input())
    z, x = 1, 2
    while z != 0 and x < X-1:
        z = X % x
        x += 1
    if X == 0 or X == 1 or z == 0:
        print('{} nao eh primo'.format(X))
    else:
        print('{} eh primo' .format(X))