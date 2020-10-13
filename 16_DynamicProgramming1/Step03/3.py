N=int(input())

dp = [0] * 1000001
dp[1], dp[2] = 1, 2 #1, 2번째 점화식 값 지정

for i in range(3,N+1):
    dp[i] = (dp[i-1] + dp[i-2])%15746 #1, 2, 3, 5, 8...으로 나가는 점화식 
print(dp[N])

