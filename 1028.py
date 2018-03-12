import math

N = int(input())

for x in range(N):
    A, B = input().split(' ')
    A, B = int(A), int(B)
    print(math.gcd(A, B))
