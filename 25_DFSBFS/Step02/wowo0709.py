import sys
input = sys.stdin.readline

def dfs(v):
    visited[v] = 1
    for i in range(1,N+1):
        if (not visited[i]) and (graph[v][i]):
            visited[i] = 1
            dfs(i)


N = int(input())
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
M = int(input())
for _ in range(M):
    x,y = map(int,input().split())
    graph[x][y] = graph[y][x] = 1

dfs(1)
print(sum(visited)-1)