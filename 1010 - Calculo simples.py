p1 = input('')
c1, np1 , vp1 = p1.split(' ')
p2 = input('')
c2, np2 , vp2 = p2.split(' ')

pagar = (int(np1)*float(vp1))+(int(np2)*float(vp2))


print('VALOR A PAGAR: R$ {:.2f}' .format(pagar))
