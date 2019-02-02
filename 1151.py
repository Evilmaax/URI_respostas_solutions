N = int(input())
x, b, a = 0, 1, 0

while x < N:
    if x < N-1:
        print('{}'.format(a), end=' ')
        a, b = b, a + b
        x += 1
    else:
        print('{}'.format(a))
        x += 1