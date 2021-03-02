#992ms
import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())

max_size = E*10 + 1
graph = {i + 1: [] for i in range(V)}
shortest_path = [max_size for _ in range(V + 1)]
shortest_path[K] = 0

for e in range(E):
	u, v, w = map(int, sys.stdin.readline().split())
	graph[u].append((v,w))


cur = []
heapq.heappush(cur, [0, K])
while cur:
	c = heapq.heappop(cur)
	for v, w in graph[c[1]]:
		tmp_w = c[0] + w
		if shortest_path[v] > tmp_w:
			shortest_path[v] = tmp_w
			heapq.heappush(cur, [tmp_w, v])

for i in range(1, V + 1):
	if shortest_path[i] == max_size:
		print("INF")
	else:
		print(shortest_path[i])
