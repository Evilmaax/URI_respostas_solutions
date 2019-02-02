X, Y = input().split(' ')
X, Y, seq = int(X), int(Y), 1

while seq in range(1, Y):
    z = 0
    for z in range(1, X+1):
        if z < X:
            print('{}'.format(seq), end=' ')
        else:
            print(seq)
        z += 1
        seq += 1