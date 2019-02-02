from fractions import Fraction
N = int(input())

for x in range(N):
    nums = input().split(' ')
    if nums[3] == '+':
        N1, N2 = nums[0], nums[4]
        op = nums[3]
        D1, D2 = nums[2], nums[6]
        first = int(N1)*int(D2) + int(N2)*int(D1)
        sec = int(D1)*int(D2)
        f = Fraction(first, sec)
        print('{}/{} = {}/{}' .format(first, sec, f.numerator, f.denominator))
    if nums[3] == '-':
        N1, N2 = nums[0], nums[4]
        op = nums[3]
        D1, D2 = nums[2], nums[6]
        first = int(N1)*int(D2) - int(N2)*int(D1)
        sec = int(D1)*int(D2)
        f = Fraction(first, sec)
        print('{}/{} = {}/{}'.format(first, sec, f.numerator, f.denominator))
    if nums[3] == '*':
        N1, N2 = nums[0], nums[4]
        op = nums[3]
        D1, D2 = nums[2], nums[6]
        first = int(N1)*int(N2)
        sec = int(D1)*int(D2)
        f = Fraction(first, sec)
        print('{}/{} = {}/{}'.format(first, sec, f.numerator, f.denominator))
    if nums[3] == '/':
        N1, N2 = nums[0], nums[4]
        op = nums[3]
        D1, D2 = nums[2], nums[6]
        first = int(N1) * int(D2)
        sec = int(N2) * int(D1)
        f = Fraction(first, sec)
        print('{}/{} = {}/{}'.format(first, sec, f.numerator, f.denominator))