N = int(input(''))
m, s = divmod(N, 60)
h, m = divmod(m, 60)

print('{}:{}:{}' .format(h,m,s))