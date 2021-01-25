import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

answer = []
for i in range(N):
	a = A[i]
	check = False
	for j in range(i + 1,N):
		if A[j] > a:
			answer.append(A[j])
			check = True
			break
	if not check:
		answer.append(-1)
for k in answer:
	print(k, end=" ")
