import sys
input = sys.stdin.readline
from collections import deque # 시간 단축

dpos = [(0,1),(0,-1),(-1,0),(1,0)]

def bfs():
    q = deque()
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 1:
                q.append((i,j))
                riped[i][j] = 1
    while q:
        cx,cy = q.popleft()
        for dx,dy in dpos:
            nx,ny = cx+dx,cy+dy
            if 0<=nx<N and 0<=ny<M:
                if tomato[nx][ny] == 0 and not riped[nx][ny]:
                    q.append((nx,ny))
                    riped[nx][ny] = riped[cx][cy] + 1
                    

M,N = map(int,input().split())
tomato = []
tomato = [[x for x in map(int,input().split())] for _ in range(N)]
riped = [[0 for _ in range(M)] for _ in range(N)]

bfs()
max_day = 0
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 0 and not riped[i][j]:
            print(-1)
            sys.exit(0)
        max_day = max(max_day,riped[i][j])