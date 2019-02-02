N = int(input())

for x in range(0, N):
    z1, z2, z3 = input().split(' ')
    z1, z2, z3 = float(z1), float(z2), float(z3)

    print('{:.1f}'.format(((z1*2)+(z2*3)+(z3*5))/10))
