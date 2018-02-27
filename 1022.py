import fractions as F
N = int(input())

for x in range(N):
    nums = input().split(' ')
    if nums[3] == '+':
        N1, N2 = nums[0], nums[4]
        op = nums[3]
        D1, D2 = nums[2], nums[6]
        first = int(N1)*int(D2) + int(N2)*int(D1)
        sec = int(D1)*int(D2)
        fsx = repr(F.Fraction(first, sec)).split(', ')
        fsx = ', '.join(fsx).split(', ')
        print('{}/{} = {}/{}' .format(first, sec,fsx[0].strip('Fraction('), fsx[1].strip(')')))
    if nums[3] == '-':
        N1, N2 = nums[0], nums[4]
        op = nums[3]
        D1, D2 = nums[2], nums[6]
        first = int(N1)*int(D2) - int(N2)*int(D1)
        sec = int(D1)*int(D2)
        fsx = repr(F.Fraction(first, sec)).split(', ')
        fsx = ', '.join(fsx).split(', ')
        print('{}/{} = {}/{}'.format(first, sec, fsx[0].strip('Fraction('), fsx[1].strip(')')))
    if nums[3] == '*':
        N1, N2 = nums[0], nums[4]
        op = nums[3]
        D1, D2 = nums[2], nums[6]
        first = int(N1)*int(N2)
        sec = int(D1)*int(D2)
        fsx = repr(F.Fraction(first, sec)).split(', ')
        fsx = ', '.join(fsx).split(', ')
        print('{}/{} = {}/{}'.format(first, sec, fsx[0].strip('Fraction('), fsx[1].strip(')')))
    if nums[3] == '/':
        N1, N2 = nums[0], nums[4]
        op = nums[3]
        D1, D2 = nums[2], nums[6]
        first = int(N1) * int(D2)
        sec = int(N2) * int(D1)
        fsx = repr(F.Fraction(first, sec)).split(', ')
        fsx = ', '.join(fsx).split(', ')
        print('{}/{} = {}/{}'.format(first, sec, fsx[0].strip('Fraction('), fsx[1].strip(')')))