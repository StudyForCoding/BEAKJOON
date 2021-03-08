import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
dp = [[1,[a]] for a in A] # 길이,부분수열
for i in range(N-1):
    for j in range(i+1,N):
        if A[j] > A[i] and dp[i][0]+1 > dp[j][0]:
            dp[j][0] = dp[i][0] + 1
            dp[j][1] = dp[i][1] + [A[j]]
dp.sort(key=lambda x:x[0])
print(dp[N-1][0])
print(*dp[N-1][1])