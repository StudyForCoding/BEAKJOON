# 88ms
import sys
N, M = map(int, sys.stdin.readline().split())
graph = []
visited = [[0 for _ in range(M)] for _ in range(N)]

for n in range(N):
	graph.append(list(map(int, sys.stdin.readline().split()[0])))

cor = [(-1,0),(1,0),(0,-1),(0,1)]
cur = [(0,0)]
while cur:
	cur_x, cur_y = cur.pop(0)
	if cur_x == N-1 and cur_y == M-1:
		break

	for x, y in cor:
		tmp_x, tmp_y = cur_x + x, cur_y + y
		if 0 <= tmp_x < N and 0 <= tmp_y < M and not visited[tmp_x][tmp_y] and graph[tmp_x][tmp_y] == 1:
			graph[tmp_x][tmp_y] = graph[cur_x][cur_y] + 1
			cur.append((tmp_x, tmp_y))

print(graph[N-1][M-1])