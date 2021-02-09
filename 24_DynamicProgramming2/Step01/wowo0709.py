import sys
input = sys.stdin.readline

for t in range(int(input())):
    K = int(input())
    files = list(map(int,input().split()))
    dp = [[0 for _ in range(K)] for _ in range(K)]

    # d: 파일 간의 거리
    for d in range(1,K): 
        # start: 페이지 시작 지점
        for start in range(K-d):
            # end: 페이지 끝 지점
            end = start + d
            tmp = []
            # 결국 start지점부터 end지점까지의 최소값은 두 지점 사이의 임의의 i에 대하여
            # (start~i)+(i+1~end) 의 값이 가장 작을 때이다. 
            for i in range(start,end):
                tmp.append(dp[start][i]+dp[i+1][end])
            dp[start][end] = min(tmp) + sum(files[start:end+1])

    print(dp[0][K-1])