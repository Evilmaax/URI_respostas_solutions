N = int(input())

for x in range(0, N):
    z = int(input())
    if z < 0 and z % 2 != 0:
        print('ODD NEGATIVE')
    elif z < 0 and z % 2 == 0:
        print('EVEN NEGATIVE')
    elif z > 0 and z % 2 != 0:
        print('ODD POSITIVE')
    elif z > 0 and z % 2 == 0:
        print('EVEN POSITIVE')
    else:
        print('NULL')