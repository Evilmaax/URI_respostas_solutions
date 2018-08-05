from functools import lru_cache
import time

@lru_cache(maxsize=39)
def fib_com_cache(n):
    if n < 2:
        return n
    return fib_com_cache(n-1) + fib_com_cache(n-2)

def fib_ate_40(funcao):

    t1 = time.perf_counter()
    for j in range(100):
        funcao(j)
    return time.perf_counter() - t1

# Em seguida, fazemos com cache
print('Tempo de execução com cache: {:.6f} segundos'.format(fib_ate_40(fib_com_cache)))
