import sys
from collections import deque

T = int(sys.stdin.readline())

for i in range(T):
	N, M = map(int, sys.stdin.readline().split())
	queue = deque(map(int, sys.stdin.readline().split()))
	idx = deque()
	result = []
	for j in range(N):
		idx.append(j)

	while queue:
		max_queue = max(queue)
		tmp = queue.popleft()

		if tmp == max_queue:
			result.append(idx.popleft())
		else:
			queue.append(tmp)
			idx.append(idx.popleft())
	print(result.index(M) + 1)