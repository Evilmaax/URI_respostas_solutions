N, X, menor, pos = int(input()), [], 0, 0
nums = input().split(' ')

for x in range(N):
    X.append(int(nums[x]))

for z in range(X.__len__()):
    if X[z] < menor:
        menor = X[z]
        pos = z

print('Menor valor: {}' .format(menor))
print('Posicao: {}' .format(pos))