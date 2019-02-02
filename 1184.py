op = input().upper()
M, x, soma, cont = [[0 for X in range(12)] for X in range(12)], 0, 0, 0

while M[11][11] == 0:
    y = 0
    while y <= 11:
        M[x][y] = float(input())
        if y < x:
            soma += M[x][y]
            cont += 1
        y += 1
    x += 1

if op == 'S':
    print(soma)
else:
    print('{:.1f}'.format(soma / cont))
