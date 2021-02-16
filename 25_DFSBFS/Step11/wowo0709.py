import sys
input = sys.stdin.readline
from collections import deque

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1
    while q:
        v = q.popleft()
        for nv in graph[v]:
            if not visited[nv]:
                visited[nv] = -visited[v]
                q.append(nv)
            elif visited[nv] == visited[v]:
                return False
    return True

for _ in range(int(input())):
    V,E = map(int,input().split())
    graph = [set([]) for _ in range(V+1)]
    for _ in range(E):
        x,y = map(int,input().split())
        graph[x].add(y)
        graph[y].add(x)
    visited = [0 for _ in range(V+1)]
    flag = True
    for v in range(1,V+1):
        if not visited[v]:
            if not bfs(v):
                flag = False
                break

    print('YES' if flag else 'NO')