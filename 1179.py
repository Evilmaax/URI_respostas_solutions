par, impar = [], []

for x in range(15):
    aux = int(input())
    if aux % 2 == 0:
        par.append(aux)
    else:
        impar.append(aux)
    if par.__len__() == 5:
        for z in range(5):
            print('par[{}] = {}' .format(z, par[z]))
        par = []
    if impar.__len__() == 5:
        for z in range(5):
            print('impar[{}] = {}' .format(z, impar[z]))
        impar = []

for x in range(impar.__len__()):
    print('impar[{}] = {}'.format(x, impar[x]))
for x in range(par.__len__()):
    print('par[{}] = {}'.format(x, par[x]))
