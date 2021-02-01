#968ms
import sys
import bisect 
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
tmp = [A[0]]

for i in range(1, N):
	if A[i] > tmp[-1]:
		tmp.append(A[i])
	else:
		idx = bisect.bisect_left(tmp, A[i])
		tmp[idx] = A[i]
print(len(tmp))
