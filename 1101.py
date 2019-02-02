#Saídas corretas, mas não aceitas pelo URI

M, N, soma = 0, 0, 0

M, N = input().split(' ')
M, N = int(M), int(N)

if M < N:
    menor = M
    maior = N
else:
    menor = N
    maior = M

while M != 0 and N != 0:
    for c in range(menor, maior+1):
        soma += c
        print('{} ' .format(c), end="")
    print('Sum={}' .format(soma))
    soma = 0

    M, N = input().split(' ')
    M, N = int(M), int(N)

    if M < N:
        menor = M
        maior = N
    else:
        menor = N
        maior = M


#Código aceito pelo URI, mas não foi que quem criou

while True:
    try:
        m,n = list(map(int,input().split()))
        if(m < 1 or n < 1 ):
            break
        tmp = 0

        if(m > n):
            tmp = m
            m = n
            n = tmp
        soma = 0
        resultado = ''
        while(m <= n):
            resultado += str(m) + ' '
            soma += m
            m += 1
        resultado += 'Sum=%d'
        print(resultado %soma)
    except:
        break
