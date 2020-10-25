import sys
N = int(sys.stdin.readline())
arr1 = list(map(int, sys.stdin.readline().split()))
up = [1 for _ in range(N)]
down = [1 for _ in range(N)]
result = [0 for _ in range(N)]

for i in range(N):
	for j in range(i):
		if arr1[i] > arr1[j]:
			up[i] = max(up[i], up[j] + 1)
arr1.reverse()
for i in range(N):
	for j in range(i):
		if arr1[i] > arr1[j]:
			down[i] = max(down[i], down[j] + 1)
down.reverse()
for i in range(N):
    result[i] = up[i] + down[i]
print(max(result) - 1)