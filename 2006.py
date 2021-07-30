x = int(input())
acertos = 0
competidores = input().split(" ")

for y in range(5):
    if int(competidores[y]) == x:
        acertos += 1

print(acertos)