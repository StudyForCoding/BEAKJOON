import sys
input = sys.stdin.readline
from collections import deque

def dfs(cv,bv):
	visited[cv] = True

	for nv in graph[cv]:
        # backtracking
		if nv == bv: continue
		# cycle
		if (visited[nv]) or (dfs(nv,cv) == False): return False
	
	return True

# main
t = 0
while True:
    t += 1
    ans = 0
    n,m = map(int,input().split())
    if n == m == 0: sys.exit(0)
    graph = [[] for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1,n+1):
        if not visited[i] and dfs(i,0): 
            ans += 1
    print("Case {0}:".format(t),end=' ')
    if ans == 0: print("No trees.")
    elif ans == 1: print("There is one tree.")
    else: print("A forest of {0} trees.".format(ans))

