from math import factorial

x = int(input())
lista = input().split(sep = ' ')

for s in range(0, x):
    flag = 0
    s = int(lista[s])

    if s != 1:
        for i in range(2, s):
            if(s % i) == 0:
                flag = 1
                break

    if flag == 0 and s != 1:
        print(f'{s}! = {factorial(s)}')