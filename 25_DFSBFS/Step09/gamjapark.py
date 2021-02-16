#4516ms
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = []
visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(2)]

for n in range(N):
	graph.append(list(map(int, sys.stdin.readline().split()[0])))

cor = [(-1,0),(1,0),(0,-1),(0,1)]
cur = deque([(0,0,0)])
visited[0][0][0] = 1
while cur:
	cur_z, cur_x, cur_y = cur.popleft()
	if cur_x == N-1 and cur_y == M-1:
		break

	for x, y in cor:
		tmp_x, tmp_y = cur_x + x, cur_y + y
		if 0 <= tmp_x < N and 0 <= tmp_y < M:
			if visited[cur_z][tmp_x][tmp_y] == 0 and graph[tmp_x][tmp_y] == 0:
				visited[cur_z][tmp_x][tmp_y] = visited[cur_z][cur_x][cur_y] + 1
				cur.append((cur_z, tmp_x, tmp_y))
			elif cur_z == 0 and visited[1][tmp_x][tmp_y] == 0 and graph[tmp_x][tmp_y] == 1:
				visited[1][tmp_x][tmp_y] = visited[0][cur_x][cur_y] + 1
				cur.append((1, tmp_x, tmp_y))
one = visited[0][N-1][M-1]
two = visited[1][N-1][M-1]
if one == 0 and two == 0:
	print(-1)
elif one == 0 or two == 0:
	print(max(one,two))
else:
	print(min(one,two))