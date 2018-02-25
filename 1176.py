T = int(input())
x = 0

while x < T:
    N = int(input())
    z, b, a = 0, 1, 0
    while z < N:
        a, b = b, a + b
        z += 1
    print('Fib({}) = {}' .format(N, a))
    x += 1