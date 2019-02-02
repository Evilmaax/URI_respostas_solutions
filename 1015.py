from math import sqrt
x = input('')
x1, y1 = x.split(' ')
y = input('')
x2, y2 = y.split(' ')

Distancia = sqrt((float(x2)-float(x1))**2 + (float(y2)-float(y1))**2)

print('{:.4f}' .format(Distancia))