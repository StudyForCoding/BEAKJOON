'''인접 행렬로 풀이'''
import sys
input = sys.stdin.readline

def dfs(v): # 재귀
    print(v,end=' ')
    visited[v] = 1
    for i in range(1,N+1):
        if (not visited[i]) and (graph[v][i]):
            dfs(i)

def bfs(v): # 큐
    q = []
    q.append(v)
    visited[v] = 1
    while q:
        v = q.pop(0)
        print(v,end=' ')
        for i in range(1,N+1):
            if (not visited[i]) and (graph[v][i]):
                q.append(i)
                visited[i] = 1


N,M,V = map(int,input().split())
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
for _ in range(M):
    x,y = map(int,input().split())
    graph[x][y] = graph[y][x] = 1

dfs(V)
print()
for i in range(N+1): visited[i] = 0
bfs(V)