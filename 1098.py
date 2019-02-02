from decimal import Decimal as D

J1, J2, J3, I = D(1.0), D(2.0), D(3.0), D(0)

while I <= 2:
    print('I={} J={}'.format(I, J1).strip('0').strip('.').replace('2.0','2').replace('1.0','1'))
    print('I={} J={}'.format(I, J2).strip('0').strip('.').replace('2.0','2').replace('1.0','1'))
    print('I={} J={}'.format(I, J3).strip('0').strip('.').replace('2.0','2').replace('1.0','1'))
    J1 += D("0.2")
    J2 += D("0.2")
    J3 += D("0.2")
    I += D("0.2")