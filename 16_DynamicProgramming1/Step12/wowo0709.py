import sys
n = int(input())
a = list(map(int,sys.stdin.readline().split()))
dp_inc = [0]*n
dp_dec = [0]*n
dp_inc[0] = dp_dec[-1] = 1
for i in range(1,n):
    maxlen_inc = 0
    maxlen_dec = 0
    for j in range(i):
        if a[j] < a[i] and maxlen_inc < dp_inc[j]:
            maxlen_inc = dp_inc[j]
        if a[-(j+1)] < a[-(i+1)] and maxlen_dec < dp_dec[-(j+1)]:
            maxlen_dec = dp_dec[-(j+1)] 
    dp_inc[i] = maxlen_inc + 1
    dp_dec[-(i+1)] = maxlen_dec + 1
dp = [dp_inc[i] + dp_dec[i] - 1 for i in range(n)]
print(max(dp))