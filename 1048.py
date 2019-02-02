x = float(input())
reajuste = 0

if x <= 400:
    reajuste = 15
    novo = x + x*0.15
elif x <= 800:
    reajuste = 12
    novo = x + x * 0.12
elif x <= 1200:
    reajuste = 10
    novo = x + x * 0.10
elif x <= 2000:
    reajuste = 7
    novo = x + x * 0.07
else:
    reajuste = 4
    novo = x + x * 0.04

print('Novo salario: {:.2f}' .format(novo))
print('Reajuste ganho: {:.2f}' .format(novo - x))
print('Em percentual: {} %' .format(reajuste))