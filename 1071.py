x = int(input())
y = int(input())

soma = 0

if x < y:
    menor = x
    maior = y
else:
    menor = y
    maior = x

for c in range(menor+1, maior):
    if c % 2 != 0:
        soma += c

print(soma)