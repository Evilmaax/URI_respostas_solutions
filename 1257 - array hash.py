rodadas = int(input())
alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


for x in range(rodadas):
    step = int(input())
    soma, cont = 0, 0
    for step in range(step):
        posi = 0
        code = input()
        for y in code:
            soma += int(alfabeto.index(y)) + cont + posi
            posi += 1
        cont +=1
    print(soma)
