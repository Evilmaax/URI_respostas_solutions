N = int(input())

for x in range(1, N+1):
    num = int(input())
    soma = 0
    for z in range(1, num):
        if num % z == 0:
            soma += z
    if soma == num:
        print('{} eh perfeito'.format(num))
    else:
        print('{} nao eh perfeito'.format(num))