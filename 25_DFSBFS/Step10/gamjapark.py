# 3448ms
import sys
from collections import deque

T = int(sys.stdin.readline())
for t in range(T):
	l = int(sys.stdin.readline())
	start_x, start_y = map(int, sys.stdin.readline().split())
	end_x, end_y = map(int, sys.stdin.readline().split())
	graph = [[0 for _ in range(l)] for _ in range(l)]
	
	cur = deque([(start_x, start_y)])
	cor = [(-2, 1),(-1,2),(1,2),(2, 1),(1, -2),(2, -1),(-1,-2),(-2,-1)]
	if start_x == end_x and start_y == end_y:
		print(0)
		continue

	while cur:
		cur_x, cur_y = cur.popleft()
		if cur_x == end_x and cur_y == end_y:
			print(graph[cur_x][cur_y])
			break

		for x, y in cor:
			tmp_x, tmp_y = cur_x + x, cur_y + y
			if 0 <= tmp_x < l and 0 <= tmp_y < l and not graph[tmp_x][tmp_y]:
				graph[tmp_x][tmp_y] = graph[cur_x][cur_y] + 1
				cur.append((tmp_x, tmp_y))