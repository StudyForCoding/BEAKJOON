import sys
N = int(sys.stdin.readline())
arr1=[]
for i in range(N):
	arr1.append(list(map(int, sys.stdin.readline().split())))

result = [1 for _ in range(N)]
arr1.sort(key = lambda x: x[0])

for i in range(N):
	for j in range(i):
		if arr1[i][1] > arr1[j][1]:
			result[i] = max(result[i], result[j] + 1)
print(N - max(result))