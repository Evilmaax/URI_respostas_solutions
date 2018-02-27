N = int(input())
seq, ordem = 1, []

while N != 0:
    N = int(input()) #################################
    for x in range(N):
        a, b = input().split(' ')
        a, b = int(a), int(b)
        ordem.append('Cidade')