'''
도착지로부터 출발지까지 역으로 경로의 수를 더해간다.
경로의 모든 경우의 수를 더해야 하기 때문에 dfs를 사용한다. 
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

dx,dy = [0,0,-1,1],[1,-1,0,0]

def go_downhill(x,y):
    if x == 0 and y == 0: # 출발지(0,0)의 경로 수는 1
        return 1
    if dp[x][y] == -1: # dp 값이 -1이라면 아직 다녀가지 않은 것!
        dp[x][y] = 0
        for i in range(4): # 상하좌우에 대하여 현재 위치로 올 수 있는 경우의 수를 더한다.
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<M and 0<=ny<N:
                if h[nx][ny] > h[x][y]:
                    dp[x][y] += go_downhill(nx,ny) # 역추적
    return dp[x][y] # 현재 위치의 경로 수 반환

M,N = map(int,input().split())
h = [[x for x in map(int,input().split())] for _ in range(M)]
dp = [[-1 for _ in range(N)] for _ in range(M)]

print(go_downhill(M-1,N-1))