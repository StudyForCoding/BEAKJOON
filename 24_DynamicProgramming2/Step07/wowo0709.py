import sys
input = sys.stdin.readline

N,M = map(int,input().split())
m = list(map(int,input().split()))
c = list(map(int,input().split()))
max_c = sum(c)
# 비용에 따른 최대 확보 가능 메모리
dp = [-1 for _ in range(max_c+1)]
dp[0] = 0
# 각 앱의 비용에 대하여
for i in range(N):
    # 최대 비용에서 줄여가며
    for j in range(max_c-c[i],-1,-1): 
        if dp[j] != -1: # 이전 dp 값이 존재한다면,
            dp[j+c[i]] = max(dp[j+c[i]],dp[j]+m[i])

for i in range(max_c+1):
    if dp[i] >= M:
        print(i)
        break