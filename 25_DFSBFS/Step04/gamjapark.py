# 80ms
import sys
sys.setrecursionlimit(10000)

cor = [(-1,0),(1,0),(0,-1),(0,1)]

def solution(cur_x, cur_y):
	for y, x in cor:
		tmp_y, tmp_x = cur_y + y, cur_x + x
		if 0 <= tmp_y < M and 0 <= tmp_x < N and graph[tmp_x][tmp_y] == 1:
			graph[tmp_x][tmp_y] = -1
			solution(tmp_x, tmp_y)

T = int(sys.stdin.readline())
for t in range(T):
	M, N, K = map(int, sys.stdin.readline().split())
	graph = [[0 for _ in range(M)] for _ in range(N)]

	for k in range(K):
		X, Y = map(int, sys.stdin.readline().split())
		graph[Y][X] = 1

	cnt = 0
	for i in range(N):
		for j in range(M):
			if graph[i][j] > 0:
				solution(i, j)
				cnt += 1

	print(cnt)