import sys
A = list(map(int, sys.stdin.readline().split()))
a = []
for i in range(A[0]):
	a.append(list(map(int, sys.stdin.readline().split())))

B = list(map(int, sys.stdin.readline().split()))
b = []
for i in range(B[0]):
	b.append(list(map(int, sys.stdin.readline().split())))


c = [[0 for _ in range(B[1])] for _ in range(A[0])]
for i in range(A[0]):
	for j in range(B[1]):
		for k in range(A[1]):
			c[i][j] += (a[i][k] * b[k][j])

for o in c:
	print(*o)