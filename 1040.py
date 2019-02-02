N1, N2, N3, N4 = input().split(' ')

N1, N2, N3, N4 = float(N1), float(N2), float(N3), float(N4)

MEDIA = (N1*0.2)+(N2*0.3)+(N3*0.4)+(N4*0.1)

if MEDIA >= 7:
    print('Media: {:.1f}' .format(MEDIA))
    print('Aluno aprovado.')
elif MEDIA < 5:
    print('Media:', int(10 * (N1*.2 + N2*.3 + N3*.4 + N4*.1)) / 10)
    print('Aluno reprovado.')
else:
    EXAME = float(input(''))
    print('Media: {:.1f}'.format(MEDIA))
    print("Aluno em exame.")
    print('Nota do exame: {:.1f}'.format(EXAME))
    MEDIAF = (MEDIA + EXAME) / 2
    if MEDIAF >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print('Media final: {:.1f}'.format(MEDIAF))
