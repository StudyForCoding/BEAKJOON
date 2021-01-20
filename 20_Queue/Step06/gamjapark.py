import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

nums = deque()

for i in range(1, N + 1):
	nums.append(i)

removed = list(map(int, sys.stdin.readline().split()))
answer = 0

for r in removed:
	tot = len(nums)
	idx = nums.index(r)
	if tot // 2 >= idx:
		for i in range(idx):
			nums.append(nums.popleft())
			answer += 1
		nums.popleft()
	else:
		for i in range(tot - idx):
			nums.appendleft(nums.pop())
			answer += 1
		nums.popleft()

print(answer)
