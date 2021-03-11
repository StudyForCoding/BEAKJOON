import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
m = int(input())
dp = [[[INF,[]] for _ in range(n+1)] for _ in range(n+1)] # 최소비용, 경로 
for _ in range(m):
    a,b,c = map(int,input().split())
    if c < dp[a][b][0]: dp[a][b][0] = c
# floyd-warshall algorithm
for byV in range(1,n+1):
    dp[byV][byV][0] = 0
    for fromV in range(1,n+1):
        for toV in range(1,n+1):
            if fromV == toV: continue
            if byV == 1: dp[fromV][toV][1] = [fromV,toV]
            if dp[fromV][byV][0]+dp[byV][toV][0] < dp[fromV][toV][0]:
                dp[fromV][toV][0] = dp[fromV][byV][0]+dp[byV][toV][0]
                dp[fromV][toV][1] = dp[fromV][byV][1][:-1]+dp[byV][toV][1][:]
# 출력
paths = []
for fromV in range(1,n+1):
    for toV in range(1,n+1):
        print(dp[fromV][toV][0] if dp[fromV][toV][0] != INF else 0,end=' ')
        paths.append(dp[fromV][toV][1])
    print()
for path in paths:
    print(len(path),*path)



