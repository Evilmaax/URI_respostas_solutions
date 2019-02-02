alcool, gasolina, diesel, x = 0, 0, 0, 0

while x <= 0 or x > 4:
    x = int(input())
    while x != 4:
        x = int(input())
        if x == 1:
            alcool += 1
        elif x == 2:
            gasolina += 1
        elif x == 3:
            diesel += 1

print('MUITO OBRIGADO')
print('Alcool: {}' .format(alcool))
print('Gasolina: {}' .format(gasolina))
print('Diesel: {}' .format(diesel))