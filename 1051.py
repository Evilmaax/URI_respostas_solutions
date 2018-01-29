#método 1

x = float(input())
p1 = 0
p2 = 0
p3 = 0
if x <= 2000.00:
    print('Insento')
elif 2000.01 <= x <= 3000:
    p1 = x - 2000.0
elif 3000.01 <= x <= 4500:
    p1 = 1000
    p2 = x - 3000.0
else:
    p1 = 1000
    p2 = 1500
    p3 = x - 4500.0

if p1 != 0:
    print('R$ {:.2f}'.format(p1*0.08 + p2*0.18 + p3*0.28))



# Método 2


x = float(input())
imposto, resto = 0, 0

if x < 4500:
    resto = x

if x > 4500:
    imposto = imposto + ((x - 4500) * 0.28)
    resto = 4500
if (x <= 4500 and x > 3000) or (resto <= 4500 and resto > 3000):
    imposto = imposto + ((resto - 3000) * 0.18)
    resto = 3000
if (x <= 3000 and x > 2000) or (resto <= 3000 and resto > 2000):
    imposto = imposto + ((resto - 2000) * 0.08)

if imposto == 0:
    print('Isento')
else:
    print('R$ {:.2f}' .format(imposto))
