import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))

result = [[0 for _ in range(15001)] for _ in range(31)]

def solve(cur, weight):
	if result[cur][weight]:
		return

	result[cur][weight] = 1

	if cur == n:
		return

	solve(cur+1, weight+arr[cur])
	solve(cur+1, weight)
	solve(cur+1, abs(weight-arr[cur]))
	
solve(0,0)
for c in check:
	if c > 15000:
		print("N", end=" ")
	elif result[n][c]:
		print("Y", end=" ")
	else:
		print("N", end=" ")