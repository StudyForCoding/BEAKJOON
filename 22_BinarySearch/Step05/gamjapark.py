# 636ms
import sys
N, C = map(int, sys.stdin.readline().split())
x_cor = [int(sys.stdin.readline()) for _ in range(N)]
x_cor.sort()

minLen, maxLen = 1, x_cor[-1] - x_cor[0]
while minLen <= maxLen:
	mid = (maxLen+minLen) // 2
	x = x_cor[0]
	count = 1
	for i in range(1, N):
		if x_cor[i] - x >= mid:
			count += 1
			x = x_cor[i]
		if count >= C:
			answer = mid
			minLen = mid + 1
			break

	if count < C:
		maxLen = mid -1
print(answer)
	