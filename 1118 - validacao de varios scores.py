N1 = -1
N2 = -1
x = 1

while x != 2:
    N1 = -1
    N2 = -1
    while N1 < 0 or N1 > 10:
        N1 = float(input())
        if N1 < 0 or N1 >10:
            print('nota invalida')
    while N2 < 0 or N2 > 10:
        N2 = float(input())
        if N2 < 0 or N2 >10:
            print('nota invalida')
    print('media = {:.2f}' .format((N1+N2)/2))
    print('novo calculo (1-sim 2-nao)')
    x = int(input())
    while x != 1 and x != 2:
        print('novo calculo (1-sim 2-nao)')
        x = int(input())