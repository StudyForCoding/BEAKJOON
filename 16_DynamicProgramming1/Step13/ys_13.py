N = int(input())
a = []
b = []
dp = [0 for i in range(N)]
#겹치지 않는 최대 전깃줄 수 구해서 N에서 뺌(LIS문제)

for i in range(N):
    a.append(list(map(int, input().split())))
a.sort(key = lambda x:x[0])
#A전봇대 기준으로 sort->b수열에서 가장 긴 증가하는 부분수열 구하면됨

for i in range(N):
    b.append(a[i][1])
for i in range(N):
    for j in range(i):
        if b[i] > b[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(N - max(dp))
