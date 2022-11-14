X = []

for x in range(10):
    X.append(int(input()))
    if X[x] <= 0:
        X[x] = 1

for x in range(10):
    print('X[{}] = {}' .format(x, X[x]))
