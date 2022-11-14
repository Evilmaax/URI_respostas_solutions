while int(input()) != 0:
    lista = input().split(sep=' ')
    pico = 0
    anterior = 0

    if int(lista[-1]) > int(lista[0]):
        tendencia = 1
    else:
        tendencia = 0

    if len(lista) == 2:
        pico = 2
    else:
        lista.append(lista[0])
        lista = [int(i) for i in lista]

        for x in range(0, len(lista)-1):
            if tendencia == 0:
                if lista[x+1] > lista[x]:
                    anterior = tendencia
                    tendencia = 0
                else:
                    anterior = tendencia
                    tendencia = 1
                if anterior != tendencia:
                    pico += 1
            else:
                if lista[x + 1] > lista[x]:
                    anterior = tendencia
                    tendencia = 0
                else:
                    anterior = tendencia
                    tendencia = 1
                if anterior != tendencia:
                    pico += 1

    print(pico)


# Solução otimizada

# while True:
#     n = int(input())
#     if n == 0:
#         break
#     h = [int(x) for x in input().split()]
#     h.append(h[0])
#     h.append(h[1])
#     picos = 0
#     for i in range(1, n + 1):
#         if h[i] < h[i - 1] and h[i] < h[i + 1]:
#             picos += 1
#         elif h[i] > h[i - 1] and h[i] > h[i + 1]:
#             picos += 1
#     print(picos)