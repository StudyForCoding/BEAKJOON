import sys
n = int(input())
l = [[int(num) for num in sys.stdin.readline().split()] for line in range(n)]
l.sort(key=lambda x:x[0])
dp = [0]*n;dp[0] = 1
for i in range(1,n):
    maxlen = 0
    for j in range(i):
        if l[j][1] < l[i][1] and maxlen <dp[j]:
            maxlen = dp[j]
    dp[i] = maxlen + 1
print(n-max(dp))