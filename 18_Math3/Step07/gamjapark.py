import sys
N, K = map(int, sys.stdin.readline().split())

def bino(N, K):
	tmp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
	for i in range(N + 1):
		tmp[i][0] = 1
	for i in range(K + 1):
		tmp[i][i] = 1
	for i in range(2, N + 1):
		for j in range(1, K + 1):
			tmp[i][j] = tmp[i - 1][j] + tmp[i - 1][j - 1]
	return tmp[N][K]
print(bino(N, K))
