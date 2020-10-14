import sys 
N = int(sys.stdin.readline())
arr1 = list(map(int, sys.stdin.readline().split()))
result = [0 for _ in range(N)]
result[0] = arr1[0]

for i in range(1, N):
	result[i] = max(arr1[i], arr1[i] + result[i-1])

print(max(result))