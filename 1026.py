#Método usando bitwise

import sys

for line in sys.stdin:
    X, Z = [int(i) for i in line.split()]
    print(X^Z)





_________________________________________________________

#método no braço

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