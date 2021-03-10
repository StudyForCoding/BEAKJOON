import sys
input = sys.stdin.readline
from collections import deque

def bfs(x):
    q = deque()
    q.append(x)
    while q:
        cx = q.popleft()
        if cx == K: return dp[K][0]
        for nx in [cx-1,cx+1,cx*2]:
            if 0<=nx<=100000 and dp[nx][0] == -1:
                dp[nx][0] = dp[cx][0]+1
                dp[nx][1] = cx # dp[toX][1] = fromX
                q.append(nx)

N,K = map(int,input().split())
dp = [[-1,-1] for _ in range(100001)] # 횟수, 이전 위치
dp[N][0] = 0
cnt = bfs(N)
toX,path = K,[K]
while dp[toX][1] != -1:
    path.append(dp[toX][1])
    toX = dp[toX][1]
print(cnt)
print(*path[::-1])
    

    