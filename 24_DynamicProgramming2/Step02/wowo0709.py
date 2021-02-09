import sys
input = sys.stdin.readline

N = int(input())
sizes = [[x for x in map(int,input().split())] for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]

for d in range(1,N):
    for start in range(N-d):
        end = start + d
        for i in range(start,end): 
            tmp = dp[start][i]+dp[i+1][end]+(sizes[start][0]*sizes[i][1]*sizes[end][1])
            if i == start:  
                dp[start][end] = tmp
            else:
                dp[start][end] = tmp if dp[start][end] > tmp else dp[start][end]

print(dp[0][N-1])