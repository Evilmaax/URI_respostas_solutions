A, B, C = input().split()
A, B, C = float(A), float(B), float(C)

if A < (B + C) and B < (A + C) and C < (A + B):
    print('Perimetro = {:.1f}' .format(A+B+C))
else:
    print('Area = {:.1f}' .format((A+B)*C/2))