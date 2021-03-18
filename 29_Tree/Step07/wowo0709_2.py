import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    cnt = 0
    visited = [[0,0] for _ in range(n+1)] # visited, fromV
    q = deque()
    for i in range(1,n+1):
        if visited[i][0]: continue
        q.append(i)
        visited[i][0] = 1
        tree_flag = True
        while q:
            cv = q.popleft()
            for nv in graph[cv]:
                # backtracking
                if nv == visited[cv][1]: continue
                # cycle
                if visited[nv][0]:
                    tree_flag = False
                    q.clear()
                    break
                # not visited
                visited[nv][0] = 1
                visited[nv][1] = cv
                q.append(nv)
        if tree_flag: cnt += 1
        q.clear()
    return cnt

# main
t = 0
while True:
    t += 1
    n,m = map(int,input().split())
    if n == m == 0: sys.exit(0)
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    ans = bfs()
    print("Case {0}:".format(t),end=' ')
    if ans == 0: print("No trees.")
    elif ans == 1: print("There is one tree.")
    else: print("A forest of {0} trees.".format(ans))