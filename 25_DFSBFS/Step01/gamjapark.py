#352ms
import sys

N, M, V = map(int, sys.stdin.readline().split())
graph = {i:[] for i in range(1,N+1)}



for m in range(M):
	a, b = map(int, sys.stdin.readline().split())
	graph[a].append(b)
	graph[b].append(a)

for key in graph:
	graph[key].sort()

result1 = []
def dfs(cur):
	if cur in result1:
		return
	result1.append(cur)

	nodes = graph[cur]
	for node in nodes:
		dfs(node)

result2 = []
def bfs():
	cur = [V]
	while cur:
		c = cur.pop(0)
		nodes = graph[c]
		if not c in result2:
			result2.append(c)
			cur += graph[c]

dfs(V)
bfs()

print(*result1)
print(*result2)
