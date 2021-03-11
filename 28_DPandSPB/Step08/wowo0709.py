import sys
input = sys.stdin.readline
from heapq import heappush,heappop
INF = sys.maxsize

def dijkstra(v):
    hp = []
    heappush(hp,(0,v))
    while hp:
        cc,cv = heappop(hp)
        if dp[cv][0] < cc: continue
        for nc,nv in graph[cv]:
            tmp_c = cc+nc
            if dp[nv][0] <= tmp_c: continue
            dp[nv][0] = tmp_c
            dp[nv][1] = dp[cv][1]+[nv]
            heappush(hp,(tmp_c,nv))
# main
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
dp = [[INF,[]] for _ in range(n+1)] # 최소비용, 경로
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
fromV,toV = map(int,input().split())
dp[fromV][0],dp[fromV][1] = 0,[fromV]
dijkstra(fromV)
print(dp[toV][0])
print(len(dp[toV][1]))
print(*dp[toV][1])