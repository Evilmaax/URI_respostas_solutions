A = []

for x in range(100):
    A.append(float(input()))

for x in range(100):
    if A[x] <= 10:
        print('A[{}] = {:.1f}'.format(x, A[x]))