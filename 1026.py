import sys

for line in sys.stdin:
    X, Z = [int(i) for i in line.split()]
    print(X^Z)