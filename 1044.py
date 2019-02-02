A, B = input('').split(' ')
A, B = float(A), float(B)

if A % B == 0 or B % A == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')