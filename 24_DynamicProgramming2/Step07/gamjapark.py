import sys
N, M = map(int, sys.stdin.readline().split())
m = [0]+ list(map(int, sys.stdin.readline().split()))
c = [0] + list(map(int, sys.stdin.readline().split()))

tot = sum(c)
result = [[0 for _ in range(tot+1)] for _ in range(N+1)]

for i in range(1, N + 1):
	for j in range(1, sum(c)+ 1):
		if j < c[i]:
			result[i][j] = result[i-1][j]
		else:
			result[i][j] = max(m[i] + result[i-1][j-c[i]], result[i-1][j])
		if result[i][j] >= M:
			tot = min(tot, j)
print(tot)