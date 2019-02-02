X = input('')
A, B , C = X.split(' ')

MAIORAB = (int(A) + int(B) + abs(int(A)-int(B)))/2
MAIORAC = (MAIORAB + int(C) + abs(MAIORAB-int(C)))/2

MAIORAC = int(MAIORAC)

print('{} eh o maior' .format(MAIORAC))