rep = int(input())

for x in range(rep):
    N, K = input().split(" ")
    print(int(N) // int(K) + int(N) % int(K))