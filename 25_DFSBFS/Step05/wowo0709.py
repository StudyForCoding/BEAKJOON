import sys
input = sys.stdin.readline

dpos = [(0,1),(0,-1),(-1,0),(1,0)]

def bfs(x,y): # 최단 거리는 bfs로!
    q = []
    q.append((x,y))
    visited[x][y] = 1
    while q:
        cx,cy = q.pop(0)
        if cx == N-1 and cy == M-1:  return visited[N-1][M-1]
        for dx,dy in dpos:
            nx,ny = cx+dx,cy+dy
            if 0<=nx<N and 0<=ny<M:
                if maze[nx][ny] and not visited[nx][ny]:
                    q.append((nx,ny))
                    visited[nx][ny] = visited[cx][cy] + 1 # 거리 측정
                    

N,M = map(int,input().split())
maze = []
for _ in range(N):
    maze.append(list(map(int,list(input().rstrip()))))
visited = [[0 for _ in range(M)] for _ in range(N)]

print(bfs(0,0))