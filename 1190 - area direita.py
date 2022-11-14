op = input().upper()
M, x, y, soma, cont, controle_up, controle_down, flag, volta = [[0 for X in range(12)] for X in range(12)], 0, 0, 0, 0, 0, 11, 0, 11

while M[11][11] == 0:
    y = 0
    while y <= 11:
        M[x][y] = float(input())
        if x >= controle_up and x <= controle_down and x < y and y > volta:
            soma += M[x][y]
            cont += 1
        if x == 5 and y == 5:
            flag = 1
        y += 1
    if flag == 0:
        controle_up += 1
        controle_down -= 1
        volta -=1
    if flag == 1:
        controle_up += 1
        controle_down += 1
        volta -=1
    x += 1

if op == 'S':
    print(soma)
else:
    print('{:.1f}'.format(soma / cont))
