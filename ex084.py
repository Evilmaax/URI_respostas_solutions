lista = []
pessoa = []
maior = 0
menor = 100

while True:
    pessoa.append(str(input("Nome: ")))
    pessoa.append(float(input("Peso: ")))
    lista.append(pessoa[:])
    if pessoa[1] > maior:
        maior = pessoa[1]
    if pessoa[1] < menor:
        menor = pessoa[1]
    pessoa.clear()
    x = input(str("Quer continuar? [S/N]"))
    if x not in 'sS':
        break
print('*' * 50)
print(f'Ao todo você cadastrou {len(lista)} pessoas')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in lista:
    if p[1] == maior:
        print(p[0], end=', ')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for p in lista:
    if p[1] == menor:
        print(p[0], end=', ')
