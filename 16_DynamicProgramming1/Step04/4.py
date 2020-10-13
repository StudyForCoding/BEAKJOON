import sys
N=int(sys.stdin.readline())

dp=[0]*101

dp[1]=1
dp[2]=1
dp[3]=1

for i in range(N):
    num = int(sys.stdin.readline())
    for i in range(4, num + 1):
        dp[i] = dp[i - 2] + dp[i - 3]
    print(dp[num])
