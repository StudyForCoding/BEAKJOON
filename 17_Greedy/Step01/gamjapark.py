import sys
N, K = map(int, sys.stdin.readline().split())
arr1 = [int(sys.stdin.readline()) for _ in range(N)]

sum1 = 0
for i in range(N):
	if arr1[N-1-i] <= K:
		tmp = K // arr1[N-1-i]
		K -= arr1[N-1-i] * tmp
		sum1 += tmp
	if K == 0:
		break

print(sum1)