num, op = int(input()), input()
M = []

for x in range(12):
    col = []
    for y in range(12):
        col.append(float(input()))
        y += 1
    M.append(col)
    x += 1

if op == 'S':
    soma = 0
    for x in range(12):
        soma += M[num][x]
        x += 1
    print(soma)
else:
    soma = 0
    for x in range(12):
        soma += M[num][x]
        x += 1
    print(soma/12)