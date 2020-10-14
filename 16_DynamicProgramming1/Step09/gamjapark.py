import sys
N=int(sys.stdin.readline())

def solution(n):
	arr = [[0]*12 for _ in range(101)]
	for i in range(2, 11):
		arr[0][i] = 1

	for i in range(1, n):
		for j in range(1, 11):
			arr[i][j] = (arr[i-1][j-1] + arr[i-1][j+1])
	return sum(arr[n-1]) % 1000000000

print(solution(N))