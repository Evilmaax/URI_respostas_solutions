rep = int(input())
total = 0
menu = [1.5, 2.5, 3.5, 4.5, 5.5]

for x in range(rep):
    pedido, qtd = input().split(" ")
    total += menu[int(pedido[-1])-1] * int(qtd)

print(f'{total:.2f}')
