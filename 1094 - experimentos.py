N = int(input())

total, tcoelhos, tratos, tsapos = 0, 0, 0, 0
for x in range(0,N):
    y, c = input().split(' ')
    y = int(y)
    if c == 'C':
        tcoelhos += y
        total += y
    elif c == 'R':
        tratos += y
        total += y
    elif c == 'S':
        tsapos += y
        total += y

print('Total: {} cobaias' .format(total))
print('Total de coelhos: {}' .format(tcoelhos))
print('Total de ratos: {}' .format(tratos))
print('Total de sapos: {}' .format(tsapos))
print('Percentual de coelhos: {:.2f} %' .format(tcoelhos/total*100))
print('Percentual de ratos: {:.2f} %' .format(tratos/total*100))
print('Percentual de sapos: {:.2f} %' .format(tsapos/total*100))
