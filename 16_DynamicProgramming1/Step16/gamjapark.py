import sys
N, K = map(int, sys.stdin.readline().split())
result = [[0] * (K + 1) for _ in range(N + 1)]
arr1 = [[0, 0]]
for i in range(1, N + 1): 
	arr1.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N + 1):
	for j in range(1, K + 1):
		if j < arr1[i][0]:
			result[i][j] = result[i-1][j]
		else:
			result[i][j] = max(result[i-1][j], result[i-1][j-arr1[i][0]] + arr1[i][1])
print(result[N][K])