import sys
input = sys.stdin.readline
from collections import deque

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1
    while q:
        v = q.popleft()
        for i in range(1,N+1):
            if (not visited[i]) and (graph[v][i]):
                q.append(i)
                visited[i] = 1


N = int(input())
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
M = int(input())
for _ in range(M):
    x,y = map(int,input().split())
    graph[x][y] = graph[y][x] = 1

bfs(1)
print(sum(visited)-1)