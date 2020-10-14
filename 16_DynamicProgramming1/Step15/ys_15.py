N = int(input())
arr = list(map(int, input().split()))

dp = [x for x in arr] #입력받은 수열배열

for i in range(1, N):
    dp[i] = max(arr[i], dp[i - 1] + arr[i]) #현재값과 현재값+이전dp값 중 최대값

print(max(dp))
