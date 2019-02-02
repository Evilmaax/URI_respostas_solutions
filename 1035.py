x = input('')

A, B, C, D = x.split(' ')

if int(B) > int(C) and int(D) > int(A) and int(C) + int(D) > int(A) + int(B) and int(C) and int(D) > 0 and int(A)  % 2 == 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')