import sys
input = sys.stdin.readline

n,k = map(int,input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
dp = [0 for _ in range(k+1)] # 동전의 합이 k원이 되는 경우의 수
dp[0] = 1

for i in coins:
    for j in range(i,k+1):
        dp[j] += dp[j-i]

print(dp[k])