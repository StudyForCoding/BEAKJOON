import sys
import heapq
T = int(sys.stdin.readline())
for i in range(T):
	K = int(sys.stdin.readline())
	fileSize = list(map(int, sys.stdin.readline().split()))
	answer = [[0 for _ in range(K)] for _ in range(K)]
	sum =[0]
	for f in fileSize:
		sum.append(sum[-1] + f)

	for x in range(1, K):
		for y in range(K-x):
			answer[y][y + x] = sys.maxsize
			for z in range(y, y + x):
				answer[y][y + x] = min(answer[y][y + x], answer[y][z] + answer[z+1][y+x] + sum[y+x+1] - sum[y])
	print(answer[0][K-1])

