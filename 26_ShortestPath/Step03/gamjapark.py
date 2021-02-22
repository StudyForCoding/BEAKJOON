import sys
import heapq

T = int(sys.stdin.readline())
for ttt in range(T):
	n, m, t = map(int, sys.stdin.readline().split())
	s, g, h = map(int, sys.stdin.readline().split())

	graph = {i+1:[] for i in range(n)}
	
	for mm in range(m):
		a, b, d = map(int, sys.stdin.readline().split())
		graph[a].append((b,d))
		graph[b].append((a,d))

	Xs = [int(sys.stdin.readline()) for _ in range(t)]
	max_size = m * 1000 + 1
	def solution(N,start):
		
		shortest_path = [max_size for _ in range(N + 1)]
		shortest_path[start] = 0
		cur = []
		heapq.heappush(cur, [0, start])
		while cur:
			c = heapq.heappop(cur)
			for v, w in graph[c[1]]:
				tmp_w = c[0] + w
				if shortest_path[v] > tmp_w:
					shortest_path[v] = tmp_w
					heapq.heappush(cur, [tmp_w, v])
		return shortest_path

	g_sol, h_sol, s_sol = solution(n, g), solution(n, h), solution(n, s)
	g_s, h_s = g_sol[s], h_sol[s]
	g_h = g_sol[h]

	result = []
	for end in Xs:
		g_end, h_end, s_end = g_sol[end], h_sol[end], s_sol[end]
		if g_s == max_size or h_s == max_size or g_end == max_size or h_end == max_size:
			continue
		if g_s + h_end + g_h == s_end or h_s + g_end + g_h == s_end:
			#tmp = min(g_s + h_end, h_s + g_end) + g_h
			result.append(end)
	result.sort()
	print(*result)
		