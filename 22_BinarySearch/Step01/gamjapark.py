#796ms
import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
A.sort()

for num in nums:
	mid = N // 2
	iin = 0
	start = 0
	end = N - 1
	while mid > start or mid < end or iin:
		if num == A[mid]:
			iin = 1
			break
		elif num < A[mid]:
			end = mid-1
			mid = (end + start) // 2
		elif num > A[mid]:
			start = mid + 1
			mid = (end + start) // 2
	if A[mid] == num:
		iin = 1
	print(iin)
