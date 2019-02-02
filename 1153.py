N = int(input())
soma, z = N, N-1

for x in range(1, N-1):
    soma = soma*z
    z -= 1

print(soma)