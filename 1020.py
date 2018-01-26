X = int(input(''))

ano = X // 365
resto = X % 365
mes = resto // 30
resto = resto % 30

print('{} ano(s)' .format(ano))
print('{} mes(es)' .format(mes))
print('{} dia(s)' .format(resto))