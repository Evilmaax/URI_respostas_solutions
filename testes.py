def boundedRatio(a, l, r):
    bol = []

    for x in range(len(a)):
        flag = 0
        for y in range(l, r + 1):
            if (x+1)*y == a[x] and flag == 0:
                bol.append(True)
                flag = 1
                break

        if flag == 0:
         bol.append(False)

    return bol

a= [8,5,6, 16, 5]
l= 1
r= 3

print("resulta: ", boundedRatio(a, l, r))
print("Expected: [False, False, True, False, True]")
print("---------------------------")
a= [1, 2, 3, 4, 5]
l= 2
r= 10000

print("resulta: ", boundedRatio(a, l, r))
print("Expected: [False, False, false, False, false]")

print("---------------------------")
a= [1, 2, 3, 4, 5]
l= 1
r= 1

print("resulta: ", boundedRatio(a, l, r))
print("Expected: [True, True, True, True, True]")
