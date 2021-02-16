import sys

N = int(sys.stdin.readline())
graph = []
visited = [[0 for _ in range(N)] for _ in range(N)]
for n in range(N):
	graph.append(list(map(int, list(sys.stdin.readline().split()[0]))))

result = {}

cor = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def solution(cur_x, cur_y, cnt):
	if visited[cur_x][cur_y]:
		return

	visited[cur_x][cur_y] = 1

	if graph[cur_x][cur_y]:
		graph[cur_x][cur_y] = cnt
		try:	result[cnt] += 1
		except:	result[cnt] = 1

	for x, y in cor:
		tmp_x, tmp_y = cur_x + x, cur_y + y
		if 0 <= tmp_x < N and 0 <= tmp_y < N and not visited[tmp_x][tmp_y] and graph[tmp_x][tmp_y]:
			solution(tmp_x, tmp_y, cnt)

count = 1
for i in range(N):
	for j in range(N):
		if graph[i][j] and not visited[i][j]:
			solution(i, j, count)
			count += 1

print(len(result))
r = list(result.values())
r.sort()
for e in r:
	print(e)