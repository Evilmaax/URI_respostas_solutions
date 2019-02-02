N = float(input(''))
N = N + 0.001

cem = N // 100
resto = N % 100
cinquenta = resto // 50
resto = resto % 50
vinte = resto // 20
resto = resto % 20
dez = resto // 10
resto = resto % 10
cinco = resto // 5
resto = resto % 5
dois = resto // 2
resto = resto % 2
mum = resto // 1
resto = resto % 1
mcinq = resto // 0.50
resto = resto % 0.50
mvinte = resto // 0.25
resto = resto % 0.25
mdez = resto // 0.10
resto = resto % 0.10
mcinco = resto // 0.05
resto = resto % 0.05
mumc = resto // 0.01

print('NOTAS:')
print('{} nota(s) de R$ 100.00' .format(int(cem)))
print('{} nota(s) de R$ 50.00' .format(int(cinquenta)))
print('{} nota(s) de R$ 20.00' .format(int(vinte)))
print('{} nota(s) de R$ 10.00' .format(int(dez)))
print('{} nota(s) de R$ 5.00' .format(int(cinco)))
print('{} nota(s) de R$ 2.00' .format(int(dois)))
print('MOEDAS:')
print('{} moeda(s) de R$ 1.00' .format(int(mum)))
print('{} moeda(s) de R$ 0.50' .format(int(mcinq)))
print('{} moeda(s) de R$ 0.25' .format(int(mvinte)))
print('{} moeda(s) de R$ 0.10' .format(int(mdez)))
print('{} moeda(s) de R$ 0.05' .format(int(mcinco)))
print('{} moeda(s) de R$ 0.01' .format(int(mumc)))