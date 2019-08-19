h1, m1, h2, m2 = input().split(' ')
h1, m1, h2, m2 = int(h1), int(m1), int(h2), int(m2)

while h1+m1+h2+ m2 != 0:
    minutos, horas = 0, 0
    if h1 == h2:
        if m1 > m2:
            minutos = 1440 - (m1 - m2)
        else:
            minutos = m2 - m1

    elif m1 > m2:
        minutos = m2 + 60-m1
        if h2 - h1 >=2:
           minutos += (h2 - h1 -1)*60
        elif h1 > h2 and h2 != 0:
            horas = 24 - h1 + h2-1

    elif m2 > m1:
        minutos = m2 - m1
        if h1 > h2:
            horas = (24 - h1) + h2
        elif h1 > h2 and h2 != 0:
            horas = 24 - h1 + h2-1
        elif h2 > h1:
            minutos = (h2 - h1) * 60 + m2 - m1
        elif h2 - h1 >=2:
           minutos += (h2 - h1 -1)*60

    elif m1 == m2:
        if h1 == h2:
            minutos = 0
        elif h1 > h2:
            minutos = 1440 - ((h1 - h2) * 60)
        elif h2 > h1:
            minutos = (h2 - h1) * 60

    print(minutos + (horas*60))
    h1, m1, h2, m2 = input().split(' ')
    h1, m1, h2, m2 = int(h1), int(m1), int(h2), int(m2)