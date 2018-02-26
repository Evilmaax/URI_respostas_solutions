M = [[0 for x in range(2)] for y in range(2)]

for x in range(2):
    for y in range(2):
        y.append(int(input()))
        y += 1
    x += 1

for x in range(2):
    for y in range(2):
        print('M[{}][{}]'.format(x, y))
        y += 1
    x += 1
