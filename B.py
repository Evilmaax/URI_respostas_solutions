import sys
while True:
    N = input()
    N = N.split('-')
    if len(N) != 5:
        print('BUG')
    else:
        for x in range(1):
            if (N[x].startswith('C') or N[x].startswith('c') or N[x].endswith('C') or N[x].endswith('c')) and \
                    (N[x+1].startswith('O') or N[x+1].startswith('o') or N[x+1].endswith('O') or N[x+1].endswith('o')) and \
                    (N[x+2].startswith('B') or N[x+2].startswith('b') or N[x+2].endswith('B') or N[x+2].endswith('b')) and \
                    (N[x+3].startswith('O') or N[x+3].startswith('o') or N[x+3].endswith('O') or N[x+3].endswith('o')) and \
                    (N[x+4].startswith('L') or N[x+4].startswith('l') or N[x+4].endswith('L') or N[x+4].endswith('l')):
                print('GRACE HOPPER')
            else:
                print('BUG')