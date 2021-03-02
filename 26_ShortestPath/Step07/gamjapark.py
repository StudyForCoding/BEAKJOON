import sys

V, E = map(int, sys.stdin.readline().split())
max_size = E * (400 * 399) + 1
shortest_path = [[max_size for _ in range(V + 1)] for _ in range(V + 1)]

for e in range(E):
	a, b, c = map(int, sys.stdin.readline().split())
	shortest_path[a][b] = c

for k in range(1, V + 1):
	for i in range(1, V + 1):
		for j in range(1, V + 1):
			shortest_path[i][j] = min(shortest_path[i][j], shortest_path[i][k] + shortest_path[k][j])
ans = max_size
for i in range(1, V + 1):
	ans = min(ans, shortest_path[i][i])
print(-1 if ans == max_size else ans)