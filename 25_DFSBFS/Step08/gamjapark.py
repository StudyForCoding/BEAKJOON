import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
graph = [0 for _ in range(100001)]

cur = deque([N])

while cur:
	c = cur.popleft()
	if c == K:
		result = graph[c]
		break

	if 0 <= c-1 < 100001 and (not graph[c-1] or graph[c] + 1 < graph[c-1]):
		graph[c-1] = graph[c] + 1
		cur.append(c-1)
	if 0 <= c+1 < 100001 and (not graph[c+1] or graph[c] + 1 < graph[c+1]):
		graph[c+1] = graph[c] + 1
		cur.append(c+1)
	if 0 <= c*2 < 100001 and (not graph[c*2] or graph[c] + 1 < graph[c*2]):
		graph[c*2] = graph[c] + 1
		cur.append(c*2)
print(result)