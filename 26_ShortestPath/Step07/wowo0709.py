import sys
input = sys.stdin.readline
INF = float('inf')

V,E = map(int,input().split())
c = [[INF for _ in range(V+1)] for _ in range(V+1)]
for _ in range(E):
    a,b,c_ = map(int,input().split())
    c[a][b] = c_
# 플로이드 와샬 알고리즘 응용 -> 최단거리 사이클 탐색
for byV in range(1,V+1):
    for fromV in range(1,V+1):
        for toV in range(1,V+1):
            if c[fromV][toV] > c[fromV][byV] + c[byV][toV]:
                c[fromV][toV] = c[fromV][byV] + c[byV][toV]
ans = INF
for v in range(1,V+1): ans = min(ans,c[v][v])
print(ans if ans < INF else -1)