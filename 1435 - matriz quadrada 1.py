while True:
    N = int(input())
    if (N == 0):
        break

    M, x, valor, cont, iter, y, y_2 = [[0 for X in range(N)] for X in range(N)], 0, 1, 0, 0, 0, 0
    while iter < N/2:
        for k in range(0, N):
            for j in range(0, N):
                while y < N - cont and x < N - cont:
                    M[x][y] = valor
                    y += 1
            x += 1
            y = y_2
            if x == N:
                x = valor
                y = valor
                valor += 1
                cont += 1
                y_2 += 1
        iter += 1

    print('\n'.join([''.join(['{:3}'.format(item) for item in row])
                      for row in M]))
    print('')