#1864ms
import sys
from collections import deque
K = int(sys.stdin.readline())

for k in range(K):
	V, E = map(int, sys.stdin.readline().split())
	graph = {i+1:[] for i in range(V)}
	visited = [0 for _ in range(V + 1)]
	color = [0 for _ in range(V + 1)]

	for e in range(E):
		a, b = map(int, sys.stdin.readline().split())
		graph[a].append(b)
		graph[b].append(a)
	result = True
	for v in range(1, V+1):
		if visited[v] == 0:
			cur = deque([v])
			color[v] = 1
			while cur:
				c = cur.popleft()
				if visited[c]:
					continue
				visited[c] = 1

				for j in graph[c]:
					if visited[j] and color[c] == color[j]: #방문 and 색 같음
						result = False
						break
					elif not visited[j]:
						color[j] = -color[c]
						cur.append(j)
				if not result:
					break
		if not result:
			break
	if not result:
		print("NO")
	else:
		print("YES")
