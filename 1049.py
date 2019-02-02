classe = input()
tipo = input()
comida = input()

if classe == 'vertebrado':
    if tipo == 'ave':
        if comida == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    else:
        if comida == 'onivoro':
            print('homem')
        else:
            print('vaca')
else:
    if tipo == 'inseto':
        if comida == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    else:
        if comida == 'hematofago':
            print('sanguessuga')
        else:
            print('minhoca')