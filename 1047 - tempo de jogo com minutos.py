a, b, c, d = input('').split(' ')
a, b, c, d = int(a), int(b), int(c), int(d)

if a > 24 or c > 24 or (a == c and b == d):
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
elif a > c:
    horas = 24 - a + c
    if b > d:
        minutos = 60 - b + d
        horas -= 1
    else:
        minutos = d - b
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)' .format(horas, minutos))
elif a < c:
    horas = c - a
    if b > d:
        minutos = 60 - b + d
        horas -= 1
    else:
        minutos = d - b
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)' .format(horas, minutos))
elif a == c:
    if b > d:
        print('O JOGO DUROU 23 HORA(S) E {} MINUTO(S)' .format(60 - b + d))
    else:
        print('O JOGO DUROU 0 HORA(S) E {} MINUTO(S)'.format(d - b))
else:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')

