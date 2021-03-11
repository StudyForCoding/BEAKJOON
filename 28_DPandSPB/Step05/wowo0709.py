import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def solve(x,y):
    if x > W or y > W: return 0
    if dp[x][y] != -1: return dp[x][y]
    
    nc = max(x,y) + 1
    nx = solve(nc,y) + abs(locs[nc][0]-locs[x][0]) + abs(locs[nc][1]-locs[x][1])
    ny = solve(x,nc) + abs(locs[nc][0]-locs[y][0]) + abs(locs[nc][1]-locs[y][1])
    dp[x][y] = min(nx,ny)
    return dp[x][y]

def backtracking(x,y):
    if x > W or y > W: return
    nc = max(x,y) + 1
    nx = abs(locs[nc][0]-locs[x][0]) + abs(locs[nc][1]-locs[x][1])
    ny = abs(locs[nc][0]-locs[y][0]) + abs(locs[nc][1]-locs[y][1])

    if dp[nc][y]+nx < dp[x][nc]+ny:
        print(1)
        backtracking(nc,y)
    else:
        print(2)
        backtracking(x,nc)
    return

# main
N = int(input()) # NxN 도로
W = int(input()) # 처리해야 하는 사건의 개수
locs = [(1,1),(N,N)]
for _ in range(W): locs.append(tuple(map(int,input().split())))
dp = [[-1 for _ in range(W+2)] for _ in range(W+2)]
print(solve(0,1))
backtracking(0,1)
