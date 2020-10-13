T=int(input()) #테스트케이스 개수
arr=[]#테스트 케이스 배열
dp = [(1,0),(0,1),(1,1),(1,2)] + [(0,0) for j in range(37)]   #문제에서 N은 40까지라고 나온다. 
for i in range(T):
    N=int(input()) #테스트케이스 입력받음
    arr.append(N) #테스트케이스 배열에 추가
    for i in range(4,N+1):
        dp[i] = ( dp[i-1][0] + dp[i-2][0] , dp[i-1][1] + dp[i-2][1] )
    print(*dp[N])
