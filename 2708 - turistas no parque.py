x = input()
jeeps, turistas = 0,0

while x != 'ABEND':
    condicao, passageiros = x.split(" ")
    if condicao == 'SALIDA':
        jeeps +=1
        turistas +=int(passageiros)
    elif condicao == 'VUELTA':
        jeeps -=1
        turistas -=int(passageiros)
    x = input()

print(turistas)
print(jeeps)