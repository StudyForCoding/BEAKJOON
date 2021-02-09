import sys
sys.setrecursionlimit(10 ** 9)
M, N = map(int, sys.stdin.readline().split())
matrix = []
for i in range(M):
	matrix.append(list(map(int, sys.stdin.readline().split())))
result = [[-1 for _ in range(N)] for _ in range(M)]
result[M-1][N-1] = 1
cor = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def solve(x,y):
	if result[x][y] == -1:
		result[x][y] = 0
		for tmp_x, tmp_y in cor:
			ttmp_x, ttmp_y = x + tmp_x, y + tmp_y
			if 0 <= ttmp_x < M and 0 <= ttmp_y < N and matrix[ttmp_x][ttmp_y] < matrix[x][y]:
				result[x][y] += solve(ttmp_x, ttmp_y)
	return result[x][y]

print(solve(0,0))