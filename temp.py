import math

N = int(input())

for x in range(N):
    A, B = input().split(' ')
    A, B = int(A), int(B)
    print(math.gcd(A, B))


N = int(input())
monte, maior = [], 0

for x in range(N):
    A, B = input().split(' ')
    A, B = int(A), int(B)
    for x in range(A, 1, -1):
        if A % x == 0:
            monte.append(x)
    for x in range(len(monte)):
        if B % monte[x] == 0:
            maior = monte[x]
            break
    print(maior)