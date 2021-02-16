#68ms
import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = {i: [] for i in range(N+1)}
for m in range(M):
	a,b = map(int, sys.stdin.readline().split())
	graph[a].append(b)
	graph[b].append(a)
result = []
def dfs(cur):
	result.append(cur)
	nodes = graph[cur]
	for node in graph[cur]:
		if not node in result:
			dfs(node)
dfs(1)
print(len(result)-1)
