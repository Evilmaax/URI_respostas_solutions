N = int(input())
ins, outs = 0, 0

for x in range (0, N):
    z = int(input())
    if 10 <= z <= 20:
        ins += 1
    else:
        outs += 1

print('{} in' .format(ins))
print('{} out'.format(outs))