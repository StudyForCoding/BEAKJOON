import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

result = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
	result[i][i] = 1
for i in range(N-1):
	if nums[i] == nums[i + 1]:
		result[i][i+1] = 1
for i in range(2, N):
	for j in range(N-i):
		if nums[j] == nums[j + i] and result[j+1][j +i-1]:
			result[j][j+i] = 1
M = int(sys.stdin.readline())
for t in range(M):
	S, E = map(int, sys.stdin.readline().split())
	print(result[S-1][E-1])