maior = 0

while True:
    try:
        total = 0
        seg, ter, qua, qui, sex, sab, dom = input().split(" ")
        total += int(seg) + int(ter) + int(qua) + int(qui) + int(sex) + int(sab) + int(dom)
        if total > maior:
            maior = total
    except EOFError:
        break

print(f"{maior} = {maior:08b}") 