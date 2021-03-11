import sys
input = sys.stdin.readline
from collections import deque

def bfs(n):
    q = deque()
    q.append(n)
    while q:
        cn = q.popleft()
        if cn == 1: return dp[1][0]
        nns = [0,0,0]
        if cn % 3 == 0: nns[0] = cn//3
        if cn % 2 == 0: nns[1] = cn//2
        if n > 0 == 0: nns[2] = cn-1
        for nn in nns:
            if nn != 0 and dp[nn][0] == -1:
                dp[nn][0] = dp[cn][0]+1
                dp[nn][1] = cn
                q.append(nn)
    
# main
N = int(input())
dp = [[-1,-1] for _ in range(N+1)] # 연산횟수, 이전 숫자
dp[N][0] = 0
cnt = bfs(N)
toX,path = 1,[1]
while dp[toX][1] != -1:
    path.append(dp[toX][1])
    toX = dp[toX][1]
print(cnt)
print(*path[::-1])