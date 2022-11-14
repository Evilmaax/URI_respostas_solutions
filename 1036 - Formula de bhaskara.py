from math import  sqrt

x = input('')
A, B, C = x.split()

A, B, C = float(A), float(B), float(C)

delta = (B**2)-(4*A*C)

if A == 0 or delta < 0:
    print('Impossivel calcular')
else:
    print('R1 = {:.5f}' .format((-B+sqrt(delta))/(2*A)))
    print('R2 = {:.5f}' .format((-B-sqrt(delta))/(2*A)))