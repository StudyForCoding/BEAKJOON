import sys

N, M = map(int, sys.stdin.readline().split())
graph = {i+1 : [] for i in range(N)}


for m in range(M):
	A, B, C = map(int, sys.stdin.readline().split())
	graph[A].append((B, C))

max_size = M * 10000 + 1
min_size = M * -10000 - 1
shortest_path = [max_size for _ in range(N + 1)]
shortest_path[1] = 0

def solution():
	for _ in range(N):
		for i in range(1, N + 1):
			for v, w in graph[i]:
				if shortest_path[i] != max_size and shortest_path[v] > shortest_path[i] + w:
					shortest_path[v] = shortest_path[i] + w
	for i in range(1, N + 1):
		for v, w in graph[i]:
			if shortest_path[i] != max_size and shortest_path[v] > shortest_path[i] + w:
				return -1
	return shortest_path

if solution() == -1:
	print(-1)
else:
	for i in range(2, N + 1):
		if shortest_path[i] == max_size:
			print(-1)
		else:
			print(shortest_path[i])