N1, N2, inter, gremio, empate, grenais, x = 0, 0, 0, 0, 0, 0, 1

while x != 2:
    N1, N2 = input().split(' ')
    N1, N2 = int(N1), int(N2)
    if N1 < N2:
        gremio += 1
    elif N1 > N2:
        inter += 1
    else:
        empate += 1
    grenais += 1
    print('Novo grenal (1-sim 2-nao)')
    x = int(input())
    while x != 1 and x != 2:
        print('Novo grenal (1-sim 2-nao)')
        x = int(input())

print('{} grenais' .format(grenais))
print('Inter:{}' .format(inter))
print('Gremio:{}' .format(gremio))
print('Empates:{}' .format(empate))

if inter < gremio:
    print('Gremio venceu mais')
if inter > gremio:
    print('Inter venceu mais')
else:
    print('Nao houve vencedor')