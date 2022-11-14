N = int(input())

for x in range(1, N+1):
    if x % 2 == 0:
        print('{}^2 = {}' .format(x, x*x))