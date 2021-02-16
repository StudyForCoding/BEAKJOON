# 시간초과 deque로 해결 2608ms
import sys
from collections import deque
M, N = map(int, sys.stdin.readline().split())
graph = []
for i in range(N):
	graph.append(list(map(int, sys.stdin.readline().split())))

visited = [[0 for _ in range(M)] for _ in range(N)]

cur = deque()
cor = [(-1,0),(1,0),(0,-1),(0,1)]
for i in range(N):
	for j in range(M):
		if graph[i][j] == 1:
			cur.append((i,j))

while cur:
	cur_x, cur_y = cur.popleft()

	for x, y in cor:
		tmp_x, tmp_y = cur_x + x, cur_y + y
		if 0 <= tmp_x < N and 0 <= tmp_y < M and graph[tmp_x][tmp_y] == 0 and not visited[tmp_x][tmp_y]:
			graph[tmp_x][tmp_y] = graph[cur_x][cur_y] + 1
			cur.append((tmp_x, tmp_y))

result = 0
for g in graph:
	if 0 in g:
		result = 0
		break
	else:
		result = max(result, max(g))
print(result-1)