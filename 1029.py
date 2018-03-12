def fib (n):
    global count
    count += 1
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n -2)


N = int(input())

for i in range(N):
    x = int(input())
    count = 0
    result = fib(x)
    print("fib({}) = {} calls = {}" .format(N, (count - 1), result))