import sys

for line in sys.stdin:

    X, Z = [int(i) for i in line.split()]
    X, Z, resultado, cont, t = str(int(bin(int(X))[2:])), str(int(bin(int(Z))[2:])), [], 0, 1

    while X.__len__() != Z.__len__():
        if X.__len__() < Z.__len__():
            X = [cont] + list(X)
        else:
            Z = [cont] + list(Z)

    for x in range(X.__len__()):
        if int(X[x]) == 0 and int(Z[x]) == 0:
            resultado.append('0')
        if int(X[x]) == 1 and int(Z[x]) == 0:
            resultado.append('1')
        if int(X[x]) == 0 and int(Z[x]) == 1:
            resultado.append('1')
        if int(X[x]) == 1 and int(Z[x]) == 1:
            resultado.append('0')

    for x in reversed(resultado):
        if x == '1':
            cont += t
        t *= 2

    print(cont)


    def fib(n):
        global count
        count += 1
        if n < 2:
            return n
        else:
            return fib(n - 1) + fib(n - 2)


    N = int(input())
    num = {1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
           20}  # ,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39}
    for i in range(N):
        calc = map(fib, num)
        x = int(input())
        count = 0
        z = list(calc)
        print(z)
        # result = map(fib,x)
        print("fib({}) = {} calls = {}".format(N, (count - 1), z[x - 2]))