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


from functools import lru_cache

count = 0

@lru_cache(maxsize=39)
def fib_com_cache(n):
    global count
    count +=1
    if n < 2:
        return n
    print(count)
    return fib_com_cache(n - 1) + fib_com_cache(n - 2)



N = int(input())

for i in range(N):
    x = int(input())
    result = fib_com_cache(x)
    print("fib({}) = {} calls = {}".format(x, (count), result))
