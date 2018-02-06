x1 = int(input())
x2 = int(input())
x3 = int(input())
x4 = int(input())
x5 = int(input())

lista = [x1, x2,x3, x4, x5]
cont = 0

for c in range(0,5):
    if lista[c] % 2 == 0:
        cont += 1

print('{} valores pares' .format(cont))