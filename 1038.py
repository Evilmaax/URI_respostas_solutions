x = input('')
cod, uni = x.split(' ')

cod = int(cod)

if cod == 1:
    val = 4.00
elif cod == 2:
    val = 4.50
elif cod == 3:
    val = 5.00
elif cod == 4:
    val = 2.00
elif cod == 5:
    val = 1.50

print('Total: R$ {:.2f}' .format(val*int(uni)))