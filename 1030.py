NC = int(input())

for x in range(NC):
    n, k = map(int, input().split())
    vet = list(range(1, n + 1))
    index = k - 1

    while len(vet) > 1 and index < len(vet):
        vet.pop(index)
        index += k - 1
        if index >= len(vet):
           index %= len(vet)
    print("Case {}: {}".format(x + 1, vet[0]))
