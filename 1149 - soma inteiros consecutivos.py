z = input()
vet = z.split(' ')
A, x, soma = int(vet[0]), 1, 0
while int(vet[x]) <= 0:
    x += 1
N = int(vet[x])
x = 0
while x < N:
    soma += A + x
    x += 1
print(soma)
