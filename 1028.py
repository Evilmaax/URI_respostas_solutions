#Solução com recursividade aceita no URI

def mdc(A, B):
    return A if not B else mdc(B, A % B)

N = int(input())

for x in range(N):
    A, B = input().split(' ')
    A, B = int(A), int(B)
    print(mdc(A, B))

#Solução com a biblioteca math ainda não aceita no URI

import math

N = int(input())

for x in range(N):
    A, B = input().split(' ')
    A, B = int(A), int(B)
    print(math.gcd(A, B))
