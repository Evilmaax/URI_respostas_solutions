bandejas = int(input())
soma = 0

for x in range(bandejas):
    L, C = input().split(" ")
    L, C = int(L), int(C)
    if L > C:
        soma += C

print(soma)