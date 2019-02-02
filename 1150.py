X = int(input())
Z = int(input())
soma, cont, seq = X, 1, X

while Z <= X:
    Z = int(input())

while soma < Z:
    seq += 1
    soma += seq
    cont += 1

print(cont)