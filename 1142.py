N = int(input())*4

for z in range(1, N+1):
    if z % 4 != 0:
        print(z,'', end="")
    else:
        print('PUM')