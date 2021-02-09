import sys
input = sys.stdin.readline

N,M = map(int,input().split())
A = [0] + list(map(int,input().split()))
c = [0] + list(map(int,input().split()))
# dp[i][j]는 i번째 앱까지 중 비용 j로 얻을 수 있는 최대 메모리
dp = [[0 for _ in range(sum(c)+1)] for _ in range(N+1)]
result = sum(c)

for i in range(1,N+1):
    byte = A[i]
    cost = c[i]

    for j in range(1,sum(c)+1):
        # 현재 앱을 비활성화할만큼의 cost가 충분하지 않은 경우
        if j < cost: 
            dp[i][j] = dp[i-1][j] # 하나 이전의 앱까지만 사용
        # 같은 cost 내에서 현재 앱을 끈 뒤의 byte와 
        # 현재 앱을 끄지 않은 뒤의 byte를 비교
        else:
            dp[i][j] = max(byte+dp[i-1][j-cost],dp[i-1][j])

        if dp[i][j] >= M: # 조건이 충족된다면,
            result = min(result,j) # 더 작은 cost 값으로 갱신

if M!=0:  print(result)
else:  print(0)