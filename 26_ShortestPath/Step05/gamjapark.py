# 워셜 알고리즘 미사용시 시간초과
# 672ms
import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

max_size = M * 100000 + 1
shortest_path = [[max_size for _ in range(N + 1)] for _ in range(N + 1)]

for m in range(M):
	A, B, C = map(int, sys.stdin.readline().split())
	shortest_path[A][B] = min(shortest_path[A][B], C)

for i in range(1, N+1):
	shortest_path[i][i] = 0

def solution():
	for k in range(1, N + 1):
		for i in range(1, N + 1):
			for j in range(1, N + 1):
				shortest_path[i][j] = min(shortest_path[i][j], shortest_path[i][k] + shortest_path[k][j])
solution()
for i in range(1, N + 1):
	for j in range(1, N + 1):
		if shortest_path[i][j] == max_size:
			print(0, end=" ")
		else:
			print(shortest_path[i][j], end=" ")
	print()