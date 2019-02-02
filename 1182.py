#Método com criação de matriz e todos os índices preenchidos

M = [[0 for x in range(12)] for y in range(12)]

C, T = int(input()), input()

for x in range(12):
    for z in range(12):
        M[x][z] = float(input())

if T == 'S':
    cont = 0
    for x in range(12):
        cont += M[x][C]
    print("{:.1f}" .format(cont))
if T == 'M':
    cont = 0
    for x in range(12):
        cont += M[x][C]
    print("{:.1f}" .format(cont/12))


#Método mais simples e sem matriz criada

T = input()
soma = 0

for x in range(144):
    valor = float(input())
    if x == C:
        soma += valor
        C += 12

if T == 'S':
    print("{:.1f}" .format(soma))
else:
    print("{:.1f}" .format(soma/12))

