# 2968ms
import sys
N, M = map(int, sys.stdin.readline().split())
treeHigh = list(map(int, sys.stdin.readline().split()))

minHigh, maxHigh = 1, max(treeHigh)

answer = False
while minHigh <= maxHigh:
	mid = (minHigh + maxHigh) // 2
	sumHigh = 0
	for t in treeHigh:
		if t > mid:
			sumHigh += t - mid
		if sumHigh > M:
			minHigh = mid + 1
			break

	if sumHigh < M:
		maxHigh = mid - 1
	elif sumHigh == M:
		answer=True
		print(mid)
		break
if not answer:
	print(maxHigh)