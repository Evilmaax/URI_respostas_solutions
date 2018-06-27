valores = []

for i in range(5):
    valores.append(input('Informe um valor: '))

print('Você digitou os valores [', end='')
sep = ''
for i in range(0, len(valores)):
    print(sep, end='')
    print(f'{valores[i]}', end='')
    sep = ', '
print(']')
print('')
print('Você digitou os valores [', end='')
for i in range(len(valores)):
    if i < len(valores)-1:
        print(f'{valores[i]}', end=', ')
    else:
        print(f'{valores[i]}]')

