import sys
N = int(sys.stdin.readline())
arr1 = list(map(int, sys.stdin.readline().split()))
result = [0 for _ in range(N)]
answer = 0
for i in range(N):
	result[i] = 1
	for j in range(0, i):
		if arr1[i] > arr1[j]:
			result[i] = max(result[i], result[j] + 1)
	print(result)
	answer = max(answer, result[i])

print(answer)