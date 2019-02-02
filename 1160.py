T = int(input())

for x in range(0, T):
    PA, PB, G1, G2 = input().split(' ')
    PA, PB, G1, G2, anos = int(PA), int(PB), float(G1), float(G2), 0
    while PA <= PB and anos <= 100:
        PA += int(PA*(G1/100))
        PB += int(PB*(G2/100))
        anos += 1
    if anos <= 100:
        print('{} anos.' .format(anos))
    else:
        print('Mais de 1 seculo.')