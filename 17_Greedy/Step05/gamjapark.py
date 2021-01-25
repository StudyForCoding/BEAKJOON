import sys

N = int(sys.stdin.readline())
dis = list(map(int, sys.stdin.readline().split()))
coin = list(map(int, sys.stdin.readline().split()))

use_coin = coin[0]
tot = dis[0] * use_coin

for i in range(1, N - 1):
	if coin[i] < use_coin:
		use_coin = coin[i]
	tot += dis[i] * use_coin

print(tot)