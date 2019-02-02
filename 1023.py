N, seq, tot_p, tot_a, flag, ordem = 1, 1, 0, 0, 0, []
frase = ''

while True:
    N = int(input())
    if N == 0:
        break
    for x in range(N):
        a, b = input().split(' ')
        a, b = int(a), int(b)
        tot_p += a
        tot_a += b
        media = int(b / a)
        if len(ordem) == 0:
            cidade = [a, media]
            ordem.append(cidade)
        else:
            for z in range(len(ordem)):
                if media == ordem[z][1]:
                    ordem[z][0] += a
                    flag = 1
                    break
            if flag == 0:
                cidade = [a, media]
                ordem.append(cidade)
        flag = 0
    ordem = sorted(ordem, key=lambda x: x[1])
    if seq > 1:
        print()
    print('Cidade# {}:'.format(seq))
    for x in range(len(ordem)):
        if (x != len(ordem) - 1):
            frase = frase + str(ordem[x][0]) + "-" + str(ordem[x][1]) + " "
        else:
            frase = frase + str(ordem[x][0]) + "-" + str(ordem[x][1])
    print(frase)
    print('Consumo medio: {:.2f} m3.'.format(round(tot_a / tot_p, 2)))
    seq += 1
    ordem.clear()
    tot_p, tot_a = 0, 0
    frase = ''
