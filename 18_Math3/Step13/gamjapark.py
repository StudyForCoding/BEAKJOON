import sys
from itertools import combinations
T = int(sys.stdin.readline())


def bio(n, k):
	answer = [[0]*(i+1) for i in range(n+1)]
	for i in range(n + 1):
		answer[i][0] = 1
		answer[i][i] = 1

	for i in range(2,n + 1):
		for j in range(1, i):
			answer[i][j] = answer[i-1][j-1] + answer[i-1][j]
	return answer[n][k]

for i in range(T):
	N, M = map(int, sys.stdin.readline().split())
	print(bio(M,N))