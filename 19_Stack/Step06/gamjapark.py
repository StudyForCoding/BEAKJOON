import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

answer = [-1 for _ in range(N)]

idx = [0]
i = 1
while idx and i < N:
	while idx and A[idx[-1]] < A[i]:
		answer[idx[-1]] = A[i]
		idx.pop()
	idx.append(i)
	i += 1

for k in answer:
	print(k, end=" ")
