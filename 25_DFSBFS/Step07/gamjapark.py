# 
import sys
from collections import deque
M, N, H = map(int, sys.stdin.readline().split())
graph = [[] for i in range(H)]
for j in range(H):
	for i in range(N):
		graph[j].append(list(map(int, sys.stdin.readline().split())))

visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]

cur = deque()
cor = [(0,-1,0),(0,1,0),(0,0,-1),(0,0,1),(1,0,0),(-1,0,0)]
for z in range(H):
	for i in range(N):
		for j in range(M):
			if graph[z][i][j] == 1:
				cur.append((i,j,z))

while cur:
	cur_x, cur_y, cur_z = cur.popleft()
	visited[cur_z][cur_x][cur_y] = 1
	for x, y, z in cor:
		tmp_x, tmp_y, tmp_z = cur_x + x, cur_y + y, cur_z + z
		if 0 <= tmp_x < N and 0 <= tmp_y < M and 0 <= tmp_z < H and graph[tmp_z][tmp_x][tmp_y] == 0 and not visited[tmp_z][tmp_x][tmp_y]:
			graph[tmp_z][tmp_x][tmp_y] = graph[cur_z][cur_x][cur_y] + 1
			cur.append((tmp_x, tmp_y, tmp_z))

result = -1
for z in range(H):
	for i in range(N):
		for j in range(M):
			if graph[z][i][j] == 0:
				result = 0
				break
			result = max(result, graph[z][i][j])
		if result == 0:
			break
	if result == 0:
		break


print(result-1)