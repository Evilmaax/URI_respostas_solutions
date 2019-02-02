x1 = int(input())
x2 = int(input())
x3 = int(input())
x4 = int(input())
x5 = int(input())

lista = [x1, x2,x3, x4, x5]
contPar, contI, contpos, contN = 0, 0, 0, 0

for c in range(0,5):
    if lista[c] % 2 == 0:
        contPar += 1
    else:
        contI += 1

    if lista[c] > 0:
        contpos += 1
    elif lista[c] < 0:
        contN += 1

print('{} valor(es) par(es)' .format(contPar))
print('{} valor(es) impar(es)' .format(contI))
print('{} valor(es) positivo(s)' .format(contpos))
print('{} valor(es) negativo(s)' .format(contN))