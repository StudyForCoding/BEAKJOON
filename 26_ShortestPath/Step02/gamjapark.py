import sys
import heapq

N, E = map(int, sys.stdin.readline().split())

graph = {i + 1: [] for i in range(N)}
max_size = E*1000 + 1

for e in range(E):
	a, b, c = map(int, sys.stdin.readline().split())
	graph[a].append((b,c))
	graph[b].append((a,c))

v1, v2 = map(int, sys.stdin.readline().split())

def solution(start):
	shortest_path = [max_size for _ in range(N + 1)]
	shortest_path[start] = 0
	cur = []
	heapq.heappush(cur, [0, start])
	while cur:
		c = heapq.heappop(cur)
		for v, w in graph[c[1]]:
			tmp_w = c[0] + w
			if shortest_path[v] > tmp_w:
				shortest_path[v] = tmp_w
				heapq.heappush(cur, [tmp_w, v])
	return shortest_path

v1_sol = solution(v1)
v2_sol = solution(v2)
v1_1 = v1_sol[1]
v1_N = v1_sol[N]
v2_1 = v2_sol[1]
v2_N = v2_sol[N]
v1_v2 = v1_sol[v2]
if v1_1 == max_size or v1_N == max_size or v2_1 == max_size or v2_N == max_size or v1_v2 == max_size:
	print(-1)
else:
	print(min(v1_1 + v2_N, v2_1 + v1_N) + v1_sol[v2])




