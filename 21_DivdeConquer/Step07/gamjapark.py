import sys
N, B = map(int, sys.stdin.readline().split())
a = []
for i in range(N):
	a.append(list(map(lambda x: int(x) % 1000, sys.stdin.readline().split())))

def matmul(a, b):
	c = [[0 for _ in range(N)] for _ in range(N)]
	for i in range(N):
		for j in range(N):
			for k in range(N):
				c[i][j] += a[i][k] * b[k][j]
			c[i][j] %= 1000
	return c 


def solution(count):
	if count == 1:
		return a
	else:
		result = solution(int(count/2))
		result = matmul(result, result)
		
		if count % 2 == 1:
			result = matmul(result, a)
		return result

for o in solution(B):
	print(*o)