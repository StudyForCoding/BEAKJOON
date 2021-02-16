import sys
input = sys.stdin.readline
from collections import deque 

dpos = [(1,2),(2,1),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    while q:
        cx,cy = q.popleft()
        if cx == tox and cy == toy:  return visited[tox][toy]
        for dx,dy in dpos:
            nx,ny = cx+dx,cy+dy
            if 0<=nx<N and 0<=ny<N:
                if not visited[nx][ny]:
                    q.append((nx,ny))
                    visited[nx][ny] = visited[cx][cy] + 1


for _ in range(int(input())):
    N = int(input())
    visited = [[0 for _ in range(N)] for _ in range(N)]
    fromx,fromy = map(int,input().split())
    tox,toy = map(int,input().split())
    print(bfs(fromx,fromy)-1)