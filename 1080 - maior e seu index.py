maior, posicao, cont = 0, 0, 1

for x in range(0, 100):
    z = int(input())
    if z > maior:
        maior = z
        posicao = cont
        cont += 1
    else:
        cont +=1

print(maior)
print(posicao)