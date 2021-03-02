import sys
input = sys.stdin.readline
INF = float('inf')

def floyd_warshall():
    # 경유지를 가장 바깥 for문으로 하여 출발지에서 도착지로 가는 최단경로 탐색
    for byV in range(1,n+1):
        c[byV][byV] = 0
        for fromV in range(1,n+1):
            for toV in range(1,n+1):
                c[fromV][toV] = min(c[fromV][toV],c[fromV][byV]+c[byV][toV])
    return c

n,m = int(input()),int(input())
# graph = [[] for _ in range(n+1)]
c = [[INF for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a,b,c_ = map(int,input().split())
    c[a][b] = min(c[a][b],c_)

ans = floyd_warshall()
for arr in ans[1:]:
    for c in arr[1:]:
        print(c if c < INF else 0,end=' ')
    print()