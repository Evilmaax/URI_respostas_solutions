T, N, x = int(input()), [], 0

while x < 1000:
    z = 0
    while z < T and x < 1000:
        N.append(z)
        print('N[{}] = {}'.format(x, N[x]))
        z += 1
        x += 1