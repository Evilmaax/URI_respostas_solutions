a, b = input('').split(' ')
a, b = int(a), int(b)

if a > 24 or b > 24:
    print('O JOGO DUROU 24 HORA(S)')
elif a > b:
    horas = 24 - a + b
    print('O JOGO DUROU {} HORA(S)' .format(horas))
elif a < b:
    horas = b - a
    print('O JOGO DUROU {} HORA(S)'.format(horas))
else:
    print('O JOGO DUROU 24 HORA(S)')

