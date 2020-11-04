import sys
N, K =map(int, sys.stdin.readline().split())
coin = []
for i in range(N):
    coin.append(int(sys.stdin.readline()))
coin.reverse()

num =0
for j in coin:
    num += K//j
    K=K%j

print(num)