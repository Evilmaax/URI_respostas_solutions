N = int(input())
resposta = []
for x in range(N):
    a = input()
    a = list(a)
    size = len(a)
    a = ''.join(a).split(' ')
    grupo = len(a)
    if grupo == 1:
        if size == 1:
            resposta.append('a')
        elif size == 2:
            resposta.append('b')
        else:
            resposta.append('c')
    if grupo == 2:
        if size == 3:
            resposta.append('d')
        elif size == 5:
            resposta.append('e')
        else:
            resposta.append('f')
    if grupo == 3:
        if size == 5:
            resposta.append('g')
        elif size == 8:
            resposta.append('h')
        else:
            resposta.append('i')
    if grupo == 4:
        if size == 7:
            resposta.append('j')
        elif size == 11:
            resposta.append('k')
        else:
            resposta.append('l')
    if grupo == 5:
        if size == 9:
            resposta.append('m')
        elif size == 14:
            resposta.append('n')
        else:
            resposta.append('o')
    if grupo == 6:
        if size == 11:
            resposta.append('p')
        elif size == 17:
            resposta.append('q')
        else:
            resposta.append('r')
    if grupo == 7:
        if size == 13:
            resposta.append('s')
        elif size == 20:
            resposta.append('t')
        else:
            resposta.append('u')
    if grupo == 8:
        if size == 15:
            resposta.append('v')
        elif size == 23:
            resposta.append('w')
        else:
            resposta.append('x')
    if grupo == 9:
        if size == 17:
            resposta.append('y')
        else:
            resposta.append('z')
print("\n".join(resposta))








N = int(input())

for x in range(N):
    a = input()
    a = list(a)
    size = len(a)
    a = ''.join(a).split(' ')
    grupo = len(a)
    if grupo == 1:
        if size == 1:
            print('a')
        elif size == 2:
            print('b')
        else:
            print('c')
    if grupo == 2:
        if size == 3:
            print('d')
        elif size == 5:
            print('e')
        else:
            print('f')
    if grupo == 3:
        if size == 5:
            print('g')
        elif size == 8:
            print('h')
        else:
            print('i')
    if grupo == 4:
        if size == 7:
            print('j')
        elif size == 11:
            print('k')
        else:
            print('l')
    if grupo == 5:
        if size == 9:
            print('m')
        elif size == 14:
            print('n')
        else:
            print('o')
    if grupo == 6:
        if size == 11:
            print('p')
        elif size == 17:
            print('q')
        else:
            print('r')
    if grupo == 7:
        if size == 13:
            print('s')
        elif size == 20:
            print('t')
        else:
            print('u')
    if grupo == 8:
        if size == 15:
            print('v')
        elif size == 23:
            print('w')
        else:
            print('x')
    if grupo == 9:
        if size == 17:
            print('y')
        else:
            print('z')