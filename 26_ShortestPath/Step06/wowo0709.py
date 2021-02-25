import sys
input = sys.stdin.readline
INF = float('inf')
# 다익스트라 + DP로 더 짧은 시간에 풀 수 있지만 파이썬(파이썬3,Pypy3)에서는 메모리 초과..
# DP로 풀 경우 파이썬3 에서는 시간 초과..
def KCMTravel(startV):
    c = [[INF for _ in range(M+1)] for _ in range(N+1)]
    c[startV][0] = 0 # [현재 정점,사용 예산] = 최소시간
    for m in range(M+1):
        for cv in range(1,N+1):
            if c[cv][m] == INF: continue
            for t,nc,nv in graph[cv]:
                if m + nc <= M:
                    c[nv][m+nc] = min(c[cv][m]+t,c[nv][m+nc])
    return min(c[N])


for _ in range(int(input())):
    N,M,K = map(int,input().split())
    graph = [[] for _ in range(N+1)]
    hp = []
    for _ in range(K):
        u,v,c,t = map(int,input().split())
        graph[u].append((t,c,v)) # 소요시간,비용,도착점
    ans = KCMTravel(1)
    print(ans if ans < INF else 'Poor KCM')