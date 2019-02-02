X, N = int(input()), []
N.append(X)
for x in range(1, 10):
    N.append(N[x-1]*2)

for x in range(10):
    print('N[{}] = {}'.format(x, N[x]))