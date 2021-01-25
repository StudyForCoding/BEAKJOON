import sys

answer = [[[0]*21 for _ in range(21)]* 51 for _ in range(21)]

def w(a, b, c):
	if a <= 0 or b <= 0 or c <= 0:
		return 1
	if a > 20 or b > 20 or c > 20:
		return w(20, 20, 20)

	if answer[a][b][c]:
		return answer[a][b][c]
	
	if a < b < c:
		answer[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
	else:
		answer[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

	return answer[a][b][c]

while True:
	A, B, C = map(int, sys.stdin.readline().split())
	if A == -1 and B == -1 and C == -1:
		break

	print("w(%d, %d, %d) = %d"%(A, B, C, w(A, B, C)))