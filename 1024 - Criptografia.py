num = int(input())

for x in range(num):
    palavra = input()
    palavra = list(palavra)
    for z in range(palavra.__len__()):
        if ord(palavra[z]) >= 65 and ord(palavra[z]) <= 90 or ord(palavra[z]) >= 97 and ord(palavra[z]) <= 122:
            temp = ord(palavra[z])
            temp += 3
            palavra[z] = chr(temp)
    palavra.reverse()
    metade = palavra.__len__()//2
    for z in range(metade, palavra.__len__()):
        temp = ord(palavra[z])
        temp -= 1
        palavra[z] = chr(temp)
    palavra = ''.join(palavra)
    print(palavra)