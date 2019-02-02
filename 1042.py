A, B, C = input('').split()
A, B, C = int(A), int(B), int(C)

if A < B and A < C:
    first = A
elif B < A and B < C:
    first = B
else:
    first = C

if A > B and A < C or A < B and A > C:
    second = A
elif B > A and B < C or B < A and B > C:
    second = B
else:
    second = C

if A > B and A > C:
    last = A
elif B > A and B > C:
    last = B
else:
    last = C

print(first)
print(second)
print(last)
print()
print(A)
print(B)
print(C)