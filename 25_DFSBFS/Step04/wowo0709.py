import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

dpos = [(0,1),(0,-1),(-1,0),(1,0)]

def dfs(x,y):
    visited[x][y] = 1
    for dx,dy in dpos:
        nx,ny = x+dx,y+dy
        if 0<=nx<N and 0<=ny<M:
            if field[nx][ny] and not visited[nx][ny]:
                dfs(nx,ny)
    return


for _ in range(int(input())):
    M,N,K = map(int,input().split())
    field = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        x,y = map(int,input().split())
        field[y][x] = 1
    visited = [[0 for _ in range(M)] for _ in range(N)]
    ans,flg = 0,False

    for i in range(N):
        for j in range(M):
            tmp = 0
            if field[i][j] and not visited[i][j]:
                dfs(i,j)
                ans += 1
                for arr in visited:
                    tmp += sum(arr)
                if tmp == K:  flg = True # 조기 종료를 위한 코드
        if flg:
            print(ans)
            break