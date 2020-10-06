import sys
n = int(sys.stdin.readline())
triangle = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(1, n):
	arr_len = len(triangle[i])
	for j in range(arr_len):
		if j == 0:
			triangle[i][j] += triangle[i - 1][j]
		elif j == arr_len - 1:
			triangle[i][j] += triangle[i - 1][j - 1]
		else:
			triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])
print(max(triangle[n - 1]))