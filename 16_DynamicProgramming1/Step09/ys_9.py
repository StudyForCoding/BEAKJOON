N = int(input())
#각 수마다 10개씩 값을 갖는다
dp = [[0 for i in range(10)] for j in range(101)]

for i in range(1,10):
    dp[1][i] = 1 #각 자리수마다 +-1하기 위해

#카운팅  0, 9,1~8 규칙이 다름/ i:자리수, j: 맨 뒤에 갈 수 있는 경우의 수
for i in range(2,N+1):
    for j in range(10):
        if j == 0: #0이 맨뒤에 갈 수 있는
            dp[i][j] = dp[i-1][1] #경우의 수
        elif j == 9: #9가 맨 뒤에 갈 수 있는
            dp[i][j] = dp[i-1][8] #경우의 수
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]


print(sum(dp[N]) % 1000000000)

