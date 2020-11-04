import sys
n = int(input())
a = list(map(int,sys.stdin.readline().split()))
dp = [0]*n
dp[0] = 1
for i in range(1,n):
    maxlen = 0
    for j in range(i):
        if a[j] < a[i] and maxlen <dp[j]:
            maxlen = dp[j]
    dp[i] = maxlen + 1
print(max(dp))