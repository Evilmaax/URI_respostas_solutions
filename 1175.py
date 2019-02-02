N = []

for x in range(20):
    N.append(int(input()))

N.reverse()

for x in range(20):
    print('N[{}] = {}'.format(x, N[x]))