import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))
dp = [[0 for _ in range(N)] for _ in range(N)]

for d in range(N):
    for start in range(N-d):
        end = start+d
        if start == end:
            dp[start][end] = 1
            continue
        if start+1 == end:
            if nums[start] == nums[end]:
                dp[start][end] = 1
                continue
        if nums[start] == nums[end] and dp[start+1][end-1] == 1:
            dp[start][end] = 1

M = int(input())
for _ in range(M):
    S,E = map(int,input().split())
    print(dp[S-1][E-1])