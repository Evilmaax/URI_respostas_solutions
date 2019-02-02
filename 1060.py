x1 = float(input())
x2 = float(input())
x3 = float(input())
x4 = float(input())
x5 = float(input())
x6 = float(input())

lista = [x1,x2,x3,x4,x5,x6]
z = 0

for n in range (0, 6):
    if lista[n] > 0:
        z +=1

print('{} valores positivos' .format(z))