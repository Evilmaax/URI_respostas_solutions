X, N = float(input()), []
N.append(X)
for x in range(1, 100):
    N.append(N[x-1]/2)

for x in range(100):
    print('N[{}] = {:.4f}'.format(x, N[x]))