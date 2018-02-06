x1 = float(input(''))
x2 = float(input(''))
x3 = float(input(''))
x4 = float(input(''))
x5 = float(input(''))
x6 = float(input(''))

lista = [x1, x2, x3, x4 ,x5, x6]

par, cont = 0, 0

for c in range(0,6):
    if lista[c] >= 0:
        cont += 1
        par += lista[c]

print('{} valores positivos' .format(cont))
print('{:.1f}'.format(par/cont))
