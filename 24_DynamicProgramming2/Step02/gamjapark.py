import sys
N = int(sys.stdin.readline())
arr = []
for i in range(N):
	arr.append(list(map(int, sys.stdin.readline().split())))

result = [[0 for _ in range(N)] for _ in range(N)]
for i in range(1,N):
	for j in range(N-i):
		result[j][j+i] = 2**32
		for k in range(j, j+i):
			result[j][j+i] = min(result[j][j+i], result[j][k] + result[k+1][j+i] + arr[j][0]*arr[k][1]*arr[j+i][1])
print(result[0][N-1])