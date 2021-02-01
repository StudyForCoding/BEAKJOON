# 1104ms
import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

count = dict()

for a in A:
	try:	count[a] += 1
	except:	count[a] = 1

for num in nums:
	try: print(count[num], end=" ")
	except: print(0, end=" ")