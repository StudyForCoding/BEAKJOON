import sys

n = int(sys.stdin.readline())
a = [[1,1],[1,0]]
aa = [[1,0],[0,1]]

N=2
def matmul(a, b):
	c = [[0 for _ in range(N)] for _ in range(N)]
	for i in range(N):
		for j in range(N):
			for k in range(N):
				c[i][j] += a[i][k] * b[k][j]
			c[i][j] %= 1000000007
	return c 

if n <= 1:
	print(n)
else:
	t = n
	while t > 0:
		if t % 2 == 1:
			 aa = matmul(aa, a)
		a = matmul(a, a)
		t //= 2
	print(aa[0][1])