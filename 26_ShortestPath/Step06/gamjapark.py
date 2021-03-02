import sys
import heapq
T = int(sys.stdin.readline())

for _ in range(T):
	N, M, K = map(int, sys.stdin.readline().split())

	max_size = K * 1000 + 1

	graph = {i + 1: [] for i in range(N)}
	for k in range(K):
		U, V, C, D = map(int, sys.stdin.readline().split())
		graph[U].append((V, C, D))

	shortest_path = [[max_size for _ in range(M+1)] for _ in range(N+1)] # 비용, 시간
	shortest_path[1][0] = 0
	
	cococo = []
	heapq.heappush(cococo, [0, (0, 1)]) #시간, 비용, 노드
	while cococo:
		dis, cur= heapq.heappop(cococo)
		cost = cur[0]
		if cost > M or shortest_path[cur[1]][cost] < dis:
			continue

		if cur[1] == N:
			print(dis)
			break

		for v, c, d in graph[cur[1]]:
			tmp_c, tmp_d = cost + c, dis + d
			if tmp_c <= M and shortest_path[v][tmp_c] > tmp_d:
				for z in range(tmp_c + 1, M + 1):
					if shortest_path[v][z] <= tmp_d:
						break
					shortest_path[v][z] = tmp_d

				shortest_path[v][tmp_c] = tmp_d
				heapq.heappush(cococo, [tmp_d, (tmp_c, v)])
	else:
		print("Poor KCM")