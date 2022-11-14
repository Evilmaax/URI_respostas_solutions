# Yes, I could use a built in sort method, but to push my limits I made a manually and complicated sort method with
# flags to handle equal numbers

# Sim, eu podia ter feito de uma maneira bem mais simples caso usasse um método de ordenamento nativo, mas resolvi
# fazer manualmente com flags para testar meus conhecimentos. Só isso

A, B, C, = input('').split(' ')
A, B, C = float(A), float(B), float(C)
maior, menor, meio, flag = 0.0, 0.0, 0.0, 0
flag_a, flag_b, flag_c = 0, 0, 0

while flag == 0:
    if A >= B and A >= C:
        maior = A
        flag_a = 1
        flag = 1
        break
    if B >= C and B >= A:
        maior = B
        flag_b = 1
        flag = 1
        break
    if C >= B and C >= A:
        maior = C
        flag_c = 1
        flag = 1
        break
flag = 0

while flag == 0:
    if A <= B and A <= C:
        menor = A
        flag_a = 1
        flag = 1
        break
    if B <= C and B <= A:
        menor = B
        flag_b = 1
        flag = 1
        break
    if C <= B and C <= A:
        menor = C
        flag_c = 1
        flag = 1
        break
flag = 0

if flag_a == 0:
    meio = A
if flag_b == 0:
    meio = B
if flag_c == 0:
    meio = C

A, B, C = maior, meio, menor

if A >= (B+C):
    print('NAO FORMA TRIANGULO')
else:
    if A**2 == ((B**2) + (C**2)):
        print('TRIANGULO RETANGULO')
    if A**2 > ((B**2) + (C**2)):
        print('TRIANGULO OBTUSANGULO')
    if A**2 < ((B**2) + (C**2)):
        print('TRIANGULO ACUTANGULO')
    if A == B and A == C:
        print('TRIANGULO EQUILATERO')
    else:
        if A == B or A == C:
            print('TRIANGULO ISOSCELES')
        if B == C:
            print('TRIANGULO ISOSCELES')