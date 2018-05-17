op = int(input('Escolhe aí: \n\n1 - Média\n2 - Velocidade fixa\n3 - Cálculo hora\n\n'))

if op == 1:
    tempo = int(input('\nHoras: ' ))
    km = int(input('km: '))
    print('\nVelocidade média de {:.1f} km/h para fechar' .format(km/tempo))
elif op == 2:
    vel = float(input('\nVelocidade: '))
    tempo = int(input('Tempo pedalando: '))
    print('\nVai percorrer {:.1f} km nessa velocidade'.format(vel*tempo))
else:
    dist = int(input('\nDistância do trajeto: '))
    tempo = int(input('Tempo limite: '))
    parcial = 0
    for x in range(1, tempo+1):
        vm = float(input("\nVelocidade média da hora {}: " .format(x)))
        parcial += vm
        print('Percorreu {} km do percurso e faltam {}\nVelocidade média necessárias para as próximas horas: {}km' .format(parcial, dist-parcial, (dist-parcial)/tempo-x))
