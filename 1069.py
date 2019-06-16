x = int(input())

for x in range(0, x):
    mina = input()
    novamina = []
    diamante, cursor = 0, 1

    for z in mina:
        if z == '<' or z == '>':
            novamina.append(z)
    z = 0

    while cursor < len(novamina):
        if novamina[z] == '<' and novamina[z + 1] == '>':
            diamante += 1
            novamina.pop(z + 1)
            novamina.pop(z)
            z = 0
            cursor = 1
        else:
            h = 0
            if novamina[h] == '<' and novamina[h + 1] == '>':
                diamante += 1
                novamina.pop(h + 1)
                novamina.pop(h)
            z += 1
            cursor += 1
    print(diamante)
