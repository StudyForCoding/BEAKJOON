import sys
input = sys.stdin.readline

dpos = [(0,1),(0,-1),(-1,0),(1,0)]

def dfs(x,y):
    visited[x][y] = 1
    for dx,dy in dpos:
        nx,ny = x+dx,y+dy
        if 0<=nx<N and 0<=ny<N:
            if MAP[nx][ny] and not visited[nx][ny]:
                dfs(nx,ny)
    return


N = int(input())
MAP = []
for _ in range(N):
    MAP.append(list(map(int,list(input().rstrip()))))
visited = [[0 for _ in range(N)] for _ in range(N)]
ans,tmpCnt = [],0

for i in range(N):
    for j in range(N):
        Cnt = 0
        if MAP[i][j] and not visited[i][j]:
            dfs(i,j)
            for arr in visited:
                Cnt += sum(arr)
            ans.append(Cnt-tmpCnt)
            tmpCnt = Cnt
            
print(len(ans),*sorted(ans),sep='\n')