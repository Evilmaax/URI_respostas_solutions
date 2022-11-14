disp = input().split(" ")
desej = input().split(" ")
total = 0

for y in range(3):
    if int(desej[y]) > int(disp[y]):
        total += int(desej[y]) - int(disp[y])

print(total)