S, first, sec = 1, 3, 2

for x in range(1, 20):
    S += first/sec
    first += 2
    sec = sec*2

print('{:.2f}' .format(S))