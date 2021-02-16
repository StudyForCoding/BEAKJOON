import sys
input = sys.stdin.readline
from collections import deque # 시간 단축

dpos = [(0,1,0),(0,-1,0),(-1,0,0),(1,0,0),(0,0,1),(0,0,-1)] # 3차원

def bfs():
    q = deque()
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomato[i][j][k] == 1:
                    q.append((i,j,k))
                    riped[i][j][k] = 1
    while q:
        cx,cy,cz = q.popleft()
        for dx,dy,dz in dpos:
            nx,ny,nz = cx+dx,cy+dy,cz+dz
            if 0<=nx<H and 0<=ny<N and 0<=nz<M:
                if tomato[nx][ny][nz] == 0 and not riped[nx][ny][nz]:
                    q.append((nx,ny,nz))
                    riped[nx][ny][nz] = riped[cx][cy][cz] + 1
                    

M,N,H = map(int,input().split())
tomato = []
tomato = [[[x for x in map(int,input().split())] for _ in range(N)] for _ in range(H)]
riped = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]

bfs()
max_day = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 0 and not riped[i][j][k]:
                print(-1)
                sys.exit(0)
            max_day = max(max_day,riped[i][j][k])

print(max_day-1)